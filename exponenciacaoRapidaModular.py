MOD = (10 ** 9) + 7

def exponenciacaoRapida(a,b):
	
	if b == 0: return 1
	
	elif b % 2 == 0:
		
		return exponenciacaoRapida( ( a * a) % MOD, b / 2) % MOD
	
	else:
		
		return a * exponenciacaoRapida(a, b - 1) % MOD
