#libreria ZKOMM Zimple KOMMunicatios, manejador de sockets y mensajes

import socket

class elem_lista_sockets:

	ELS_OCUPADO = 0
	ELS_LISTO   = 1
	ELS_MUERTO  = 2
	ELS_MENSAJE = 3

	BUFFERSIZE  = 1024

	def __init__(self, sckt, ip, puerto, ident, open_symbol, close_symbol, verbose = False):
		self.verbose = verbose
		self.open_symbol = open_symbol
		self.close_symbol = close_symbol
		self.s_ip = ip
		self.s_puerto = puerto
		self.s_socket = sckt
		self.s_datos_i = ""
		self.s_datos_o = ""
		self.s_estado_i = self.ELS_LISTO
		self.s_estado_o = self.ELS_LISTO
		self.ident = ident
		self.mensaje = ""
		self.pid = 0

	def buscar_mensaje(self):
		#+++++++++++++++++++++++++++++++
		#Reimplementado para permitir la recepcion y eliminacion de mensajes parciales
		#de modo que un mensaje que no se haya recibido completo sea cancelado por otro
		#mas nuevo que el otro lado haya enviado. P.e.: acuses de recibo
		pos_close = self.s_datos_i.find(self.close_symbol)
		if (pos_close > 1):
			pos_open = self.s_datos_i.rfind(self.open_symbol, 0, pos_close)
			if (pos_open >= 0):
				self.mensaje = self.s_datos_i[pos_open:pos_close+1]
				self.s_datos_i = self.s_datos_i[pos_close+1:]
				return True
		return False

	def cerrar(self):
		self.s_socket.shutdown(socket.SHUT_RD)
		self.s_socket.shutdown(socket.SHUT_WR)
		self.s_socket.close()

	def recibir(self):
		if (self.verbose):
			print 'socket %d ocupado' % (self.ident)
		try:
			temp = self.s_socket.recv(self.BUFFERSIZE)
		except:
			temp = ''
		temp = temp.replace(u'\0', '')
		if (temp == ''):
			self.s_estado_i = self.ELS_MUERTO
		else:
			self.s_datos_i = self.s_datos_i + temp
			self.s_estado_i = self.ELS_LISTO
			if (self.verbose):
				print 'datos recibidos:', temp
				print 'datos en cola', self.s_datos_i

	def enviar(self):
		if (len(self.s_datos_o) > 0):
			if (self.verbose == True):
				print 'estoy enviando'
				print "longitud: ", len(self.s_datos_o)
			try :
				cont = self.s_socket.send(self.s_datos_o)
				if (self.verbose):
					print "enviados", cont, "datos"
			except:
				self.s_estado_o = self.ELS_MUERTO
			self.s_datos_o = self.s_datos_o[cont:]

