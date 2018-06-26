def exponenciacaoRapida(a,b):
	
	if b == 0: return 1
	
	elif b % 2 == 0:
		
		return exponenciacaoRapida( ( a * a) , b / 2) 
	
	else:
		
		return a * exponenciacaoRapida(a, b - 1) 
