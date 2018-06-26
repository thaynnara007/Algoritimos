#Algoritimo de Euclides:
def mdc(a,b):
	
	while (a % b != 0):
		
		aux = b
		b = a % b
		a = aux
		
	return b
	
#Algoritimo de Euclides aplicado a mmc:
def mmc(a,b):
	
	return (a * (b/mdc(a,b)))
