#zkomm_protocol
#Libreria para el protocolo de SKOMM Zimple KOMMunications

class protocolo:

	def __init__(self, starts='<', stops='>'):
		self.start_symbol=starts
		self.stop_symbol=stops

	def encoder(self, fun, args):
		ret_s = '<'+fun
		count = 0
		for s in args:
			count = count + 1
			st = ' parametro%(count)d="' % {'count':count}
			ret_s = ret_s+' parametro%(count)d="' % {'count':count}+s+'"'
		ret_s = ret_s + '>'
		return ret_s

	def decoder(self, s):
		if (len(s) > 0):
			ret_l = []
			ret_l.append(s[1:s.find(' ')])
			ret_args = []
			while (True):
				pos=s.find('"')
				if (pos > 0):
					s = s[pos+1:]
					ret_args.append(s[:s.find('"')])
					s = s[s.find('"')+1:]
				else:
					break
			ret_l.append(ret_args)
			return ret_l
		else:
			return ("",())

#test
'''
import pprint
yo = protocol()
cosa=yo.encoder("miFuncion_de_prueba",('param1', 'dato2', 'valor3', '4'))
print cosa
pprint.pprint(yo.decoder(cosa))
'''
