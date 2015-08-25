#libreria ZKOMM Zimple KOMMunicatios, manejador de sockets y mensajes

import time
import thread
import zkomm_elem_lista_sockets
import pprint
import socket

class lista_sockets:
	def __init__(self, addr, port, top=0, maxwait=3, verbose=False):
		self.verbose = verbose
		self.fin = False
		self.lista = []
		self.mensajes_i = dict()
		self.mensajes_o = dict()
		self.cont_serial=0
		self.socket_principal = socket.socket()
		self.socket_principal.bind((addr,port))
		thread.start_new_thread(self.anexa_lista,())
		thread.start_new_thread(self.revisar_lista,())

	def iniciar_conexion(self, addr, port):
		print "buscando duplicados de conexion"
		con_id = 0
		for ele in self.lista:
			if (ele.s_ip == addr):
				if (ele.s_puerto == port):
					print "Conexion duplicada: ", con_id
					return con_id
			con_id = con_id + 1
		print "conectando"
		sckt=socket.socket()
		sckt.connect((addr, port))
		return(self.anexar(sckt, addr, port, "<", ">"))

	def anexar(self, sckt, addr, port, open_symbol, close_symbol):
		if (self.verbose):
			print 'Se esta anexando en la posicion', len(self.lista), "con identificador ", self.cont_serial
		self.lista.append(zkomm_elem_lista_sockets.elem_lista_sockets(sckt, addr, port, self.cont_serial, open_symbol, close_symbol))
		self.mensajes_i[self.cont_serial]=""
		self.mensajes_o[self.cont_serial]=""
		self.cont_serial = self.cont_serial + 1
		if (self.verbose):
			print 'Anexado'
			print 'la lista tiene', len(self.lista), 'sockets'
		return (len(self.lista)-1)

	def remover(self, sckt):
		if (self.verbose):
			print "Removiendo socket %d" %(sckt.ident)
		pos = sckt.ident
		self.lista.remove(sckt)
		if (self.verbose):
			print "socket eliminado"
		self.mensajes_i.pop(pos)
		if (self.verbose):
			print "mensaje de entrada eliminado"
		self.mensajes_o.pop(pos)
		if (self.verbose):
			print "mensaje de salida eliminado"

	def anexa_lista(self):
		while not self.fin:
			if (self.verbose):
				print "Hilo principal de la lista iniciado"
			while (not self.fin):
				self.socket_principal.listen(3)
				try:
					info = self.socket_principal.accept()
					if (self.verbose):
						print "Conexion aceptada desde", info[1],"... Anexando..."

					dato=self.anexar(info[0], info[1][0], info[1][1], '<', '>')
				except:
					pass

	def enviar(self, con_id, mensaje):
		longit_ini = len(self.mensajes_o[con_id])
		self.mensajes_o[con_id] = self.mensajes_o[con_id] + mensaje
		longit_fin = len(self.mensajes_o[con_id])
		return (longit_fin - longit_ini)

	def recibir(self, con_id):
		return self.mensajes_i[con_id]

	def limpiar(self, con_id):
		self.mensajes_i[con_id] = ""
		if (self.mensajes_o[con_id] == ""):
			return True
		return False

	def detener(self):
		self.fin = True

	def revisar_lista(self):
		while (not self.fin):
			for sckt_actual in self.lista:
				ident=sckt_actual.ident
				if (self.verbose):
					print "revisando socket", ident
				if (self.mensajes_o[ident] != ""):
					if (self.verbose):
						print "Mensaje para enviar en %d" %(ident)
						print self.mensajes_o[ident]
					sckt_actual.s_datos_o += self.mensajes_o[ident]
					self.mensajes_o[ident] = ""
					thread.start_new_thread(sckt_actual.enviar,())
				if (sckt_actual.s_estado_i == sckt_actual.ELS_LISTO):
					if (self.verbose):
						print 'el socket %d va a ser escuchado' % (sckt_actual.ident)
					sckt_actual.s_estado_i = sckt_actual.ELS_OCUPADO
					thread.start_new_thread(sckt_actual.recibir,())
				if (self.mensajes_i[ident] == ""):
					if (sckt_actual.buscar_mensaje()):
						self.mensajes_i[ident] = sckt_actual.mensaje
						if (self.verbose):
							print "LISTA_SOCKETS ---- Hay mensaje en %d" %(ident)
				if ((sckt_actual.s_estado_i == sckt_actual.ELS_MUERTO) or (sckt_actual.s_estado_o == sckt_actual.ELS_MUERTO)):
					if (self.verbose):
						print 'socket %d muerto' % (ident)
					self.remover(sckt_actual)
			if (self.fin):
				break
			#No comamos todo el procesador ------------
			time.sleep(0.6)
		#si nos toca salir cerremos los sockets
		for sckt in self.lista:
			if self.verbose:
				print "Vaciando la lista de sockets"
			sckt.cerrar()
			self.remover(sckt)
		self.socket_principal.close()

if __name__=="__main__":
	yo = lista_sockets("127.0.0.1", 60000, verbose=1)
	time.sleep(1)
	yo.fin = True

