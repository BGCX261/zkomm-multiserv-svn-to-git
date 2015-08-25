#lista_nodos.nodo
#clase con la que trabaja cada nodo. Se utiliza para identificar
#cada uno de los nodos conectados

class nodo:
	def __init__(self, ident, ip, puerto, nombre="nodo", capacidad=0, carga=0, sobrecarga=0, penalizacion=0, conn_id = None):
		self.ident = ident
		self.ip = ip
		self.puerto = puerto
		self.nombre = nombre
		self.capacidad = capacidad
		self.carga = carga
		self.sobrecarga = sobrecarga
		self.penalizacion = penalizacion
		self.conn_id = conn_id

	def actualizar_datos(self, cap, c, s, p):
		self.capacidad = cap
		self.carga = c
		self.sobrecarga = s
		self.penalizacion = p

	def penalizar(self, num=1):
		self.penalizacion = self.penalizacion + num
