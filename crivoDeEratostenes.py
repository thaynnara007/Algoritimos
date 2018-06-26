maximo = 1000010
primos = [True] * maximo

def crivo(numero):
	
	global primos
	
	for i in xrange(2, numero):
		
		if primos[i]:
			
			for j in xrange(2 * i, numero , i):

				primos[j] = False
