#zkomm_servidor
#Logica interna del multiservidor ZKOMM

from zkomm_lista_sockets import *
from lista_procesadores_procesador import *
from lista_procesos_proceso import *
from lista_procesos import lista_procesos
from lista_procesadores import lista_procesadores
from lista_nodos import lista_nodos
from lista_nodos_nodo import nodo
from PyQt4 import QtCore, QtGui
#from modelo_lista_procesadores import *
import zkomm_protocol_2
import random
import thread
import time


class servidor:

	def __init__(self, verbose=False, padre = QtCore.QObject()):
		self.estado = "creado"
		self.verbose=verbose
		self.nodos_conocidos = lista_nodos([], padre)
		self.procesadores = lista_procesadores([], padre)
		self.procesos_creados = lista_procesos()
		self.procesos_cola = lista_procesos()
		self.procesos_limbo = lista_procesos()
		self.ident = 0 #Se pone temporalmente a este valor, a menos que otro nodo le ordene lo contrario
		self.protocolo = zkomm_protocol_2.protocolo()
		self.retardo = 0.5 #retardo de espera entre cada revision de las conexiones
		self.acciones = dict()

	def iniciar(self, ip, puerto):
		if (self.estado != "ejecutando"):
			self.estado = "ejecutando"
			self.lista_conexiones = lista_sockets(ip, puerto, verbose=self.verbose)
			self.acciones["recibir_datos_nodo"] = self.recibir_datos_nodo
			self.acciones["enviar_datos_nodo"] = self.enviar_datos_nodo
			self.acciones["enviar_lista_nodos"] = self.enviar_lista_nodos
			self.acciones["solicitar_lista_nodos"] = self.solicitar_lista_nodos
			self.acciones["recibir_nodo_lista"] = self.recibir_nodo_lista
			thread.start_new_thread(self.atender_conexiones, ())

	def crear_nodo_propio(self, ident, ip, puerto, nombre):
		capacidad = self.procesadores.capacidad()
		self.nodo_propio = nodo(0, ip, puerto, nombre)
		self.nodos_conocidos.agregar_nodo(self.nodo_propio)

	def detener(self):
		self.estado="detenido"
		self.lista_conexiones.detener()

	def conectar_a(self, ip, puerto):
		conexion = self.lista_conexiones.iniciar_conexion(ip, puerto)
		self.enviar_datos_nodo(conexion)
		self.solicitar_lista_nodos(conexion)

	def crear_procesadores(self, cant, Vel, VelRand, enteras=True):
		n = 0
		while (n < cant):
			if (enteras):
				v = Vel + random.randint(0, VelRand)
			else:
				v = Vel + VelRand * random.random()
			n_proc = procesador(self.ident, n, v)
			self.procesadores.agregar_procesador(n_proc)
			n = n + 1

	def recibir_datos_nodo(self, conn_id, args = ()):
		ident = None
		ip = args[1]
		puerto = args[2]
		nombre = args[3]
		capacidad = args[4]
		carga = args[5]
		sobrecarga = args[6]
		penalizacion = args[7]
		n = nodo(ident, ip, puerto, nombre, capacidad, carga, sobrecarga, penalizacion)
		if (self.nodo_propio.ip == ip):
			if (self.nodo_propio.puerto == puerto):
				self.nodo_propio = n
		if (not self.nodos_conocidos.ya_existe(n)):
			self.nodos_conocidos.agregar_nodo(n)

	def enviar_datos_nodo(self, id_con, n = None):
		if (n == None):
			n = self.nodo_propio
		cadena = self.protocolo.fun_encoder("recibir_datos_nodo", (n.ident, n.ip, n.puerto, n.nombre, n.capacidad, n.carga, n.sobrecarga, n.penalizacion))
		self.lista_conexiones.enviar(id_con, cadena)

	def enviar_lista_nodos(self, con_id, args = ()):
		print "enviando la lista de nodos"
		for nad in self.nodos_conocidos.lista:
			mensaje = self.protocolo.fun_encoder("recibir_nodo_lista", (nad.ident, nad.ip, nad.puerto, nad.nombre, nad.capacidad, nad.carga, nad.sobrecarga, nad.penalizacion))
			self.lista_conexiones.enviar(con_id, mensaje)

	def recibir_nodo_lista(self, id_con, args = ()):
		ident = args[0]
		ip = args[1]
		puerto = args[2]
		nombre = args[3]
		capacidad = args[4]
		carga = args[5]
		sobrecarga = args[6]
		penalizacion = args[7]
		if (self.verbose):
			print "Nodo de lista recibido con ID =",ident, "del  puerto",puerto
		nad = nodo(ident, ip, puerto, nombre, capacidad, carga, sobrecarga, penalizacion)
		if (nad.ip == self.nodo_propio.ip):
			if (nad.puerto == self.nodo_propio.puerto):
				if (self.verbose):
					print "Me est'an cambiando el id"
				self.procesadores.cambiar_ident_nodo(nad.ident)
		self.nodos_conocidos.actualizar_datos_nodo(nad)
		conexion = self.lista_conexiones.iniciar_conexion(ip, puerto)
		self.enviar_datos_nodo(conexion)

	def solicitar_lista_nodos(self, id_con):
		cadena = self.protocolo.fun_encoder("enviar_lista_nodos", ())
		self.lista_conexiones.enviar(id_con, cadena)

	def enviar_datos_proceso(self, conn_id, pros = None):
		if (pros == None):
			pros = self.procesos_limbo.primer_proceso()
			self.procesos_limbo.mover_al_final(pros)
		mensaje = self.protocolo.fun_encoder("recibir_datos_proceso", (pros.id_nodo, pros.ident, pros.carga))

	def enviar_proceso(self, conn_id, pros = None):

		pass

	def modelo_lista_proc(self):
		mod = self.procesadores.model()
		return (mod)

	def modelo_lista_nodos(self):
		mod = self.nodos_conocidos.model()
		return (mod)

	def modelo_lista_procesos_creados(self):
		mod = self.procesos_creados.model()
		return mod

	def modelo_lista_procesos_cola(self):
		mod = self.procesos_cola.model()
		return mod

	def crear_procesos(self, cod, cant, carga_base, rand_carga, T, rand_T):
		#Se crea un hilo para esto
		thread.start_new_thread(self.crear_procesos_hilo,(cod, cant, carga_base, rand_carga, T, rand_T))

	def crear_procesos_hilo(self, cod, cant, carga_base, rand_carga, T, rand_T):
		cont = 0
		while (cont < cant):
			n_pros = proceso(self.id_nodo, len(self.lista_procesos_creados), cod, carga_base + random.randint(0, rand_carga))
			self.procesos_creados.agregar_proceso(n_pros)
			self.procesos_cola.agregar_proceso(n_pros)
			cont = cont + 1
			time.sleep(T+random.random()*rand_T)

	def hilo_procesar_procesos(self):
		pros = self.procesos_cola.primer_proceso()
		lista_procesos.quitar_proceso(pros)

	def atender_conexiones(self):
		while (self.estado == "ejecutando"):
			for conn_id in range(0,len(self.lista_conexiones.mensajes_i)):
				texto = self.lista_conexiones.recibir(conn_id)
				if (texto != ''):
					self.lista_conexiones.limpiar(conn_id)
					accion = self.protocolo.decoder(texto)
					if (self.verbose):
						print "Texto", texto,
					print " Accion", accion[0]
					if (accion[0] in self.acciones.keys()):
						self.acciones[accion[0]](conn_id, accion[1])
			time.sleep(self.retardo)

if (__name__ == "__main__"):
	yo = servidor(verbose=True)
	cad=raw_input("Ingrese el IP de este nodo: ")
	IP = cad
	cad=raw_input("Ingrese el puerto de este nodo: ")
	prt=int(cad)
	yo.iniciar(IP, prt)
	cad=raw_input("Conectar a otro nodo: ")
	IP = cad
	cad=raw_input("Puerto remoto: ")
	prt=int(cad)
	yo.conectar_a(IP, prt)
	cad=raw_input("para salir presione ENTER")