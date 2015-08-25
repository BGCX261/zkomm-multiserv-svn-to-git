#ZKOMM Procesos
#Elementos usados en las listas de procesos y por los diferentes nodods para
#identificar sus propios procesos

class proceso:
	PROS_IDLE = 0
	PROS_EJEC = 1
	PROS_LIMBO = 2

	def __init__(self, id_nodo, ident, codigo, carga):
		self.id_nodo = id_nodo
		self.ident = ident
		self.codigo = codigo
		self.carga = carga
		self.resultado = ""
		self.estado = self.PROS_IDLE
