#zkomm_protocol
#Libreria para el protocolo de SKOMM Zimple KOMMunications

# equerido para verificar el tipo de los objetos
import operator

class protocolo:

	def __init__(self, starts='<', stops='>'):
		self.start_symbol=starts
		self.stop_symbol=stops

	def fun_encoder(self, fun, args=()):
		ret_s = '<'+fun
		count = 0
		for s in args:
			count = count + 1
			tipo = 'cad'
			if (operator.isNumberType(s)):
				s=str(s)
				tipo = 'num'
			st = ' par%(count)d="' % {'count':count}
			ret_s = ret_s+' par%(count)d="' % {'count':count}+s+'" tip%d="' % (count)+tipo+'"'
		ret_s = ret_s + '>'
		return ret_s

	def res_encoder(self, fun, result):
		ret_s = '<_resultadoDe_' + fun
		if (operator.isNumberType(result)):
			result=str(result)
			tip='num'
		else:
			tip='cad'
		ret_s = ret_s + ' val="'+result+'" tip="'+tip+'">'
		return ret_s

	def fun_decoder(self, s):
		if (len(s) > 0):
			ret_l = []
			ret_l.append(s[1:s.find(' ')])
			ret_args = []
			count = 1
			while (True):
				cadt = 'par%d' % (count)

				pos=s.find(cadt)
				pos = pos + len(cadt)

				if (len(s) > 1):
					s = s[pos+2:]
					arg=s[:s.find('"')]

					cadt = 'tip%d' % (count)
					pos = s.find(cadt)
					pos = pos + len(cadt)

					s = s[pos+2:]
					tipo = s[:s.find('"')]

					if (tipo == 'num'):
						arg=eval(arg)
					ret_args.append(arg)
					s = s[s.find('"')+1:]

					count += 1
				else:
					break
			ret_l.append(ret_args)
			return ret_l
		else:
			return ()

	def res_decoder(self, s):
		res_ini=s.find('"')+1
		res_fin=s.find('"', res_ini+1)
		res=s[res_ini:res_fin]
		s=s[res_fin+2:]
		tip_ini=s.find('"')
		tip_fin=s.find('"',tip_ini+1)
		tip=s[tip_ini+1:tip_fin]

		if (tip=="num"):
			res=eval(res)
		return res

	def decoder(self,s):
		if (s.find('<_resultadoDe_') == 0):
			return self.res_decoder(s)
		else:
			return self.fun_decoder(s)

#test

if (__name__ == "__main__"):
	import pprint
	yo = protocolo()
	cosa=yo.fun_encoder("miFuncion_de_prueba",(1, 'dato2', 'valor3', '4'))
	print cosa
	pprint.pprint(yo.decoder(cosa))
	cosa = yo.res_encoder("laFuncion",42)
	print cosa
	pprint.pprint(yo.decoder(cosa))
	raw_input("Presione ENTER para finalizar")
