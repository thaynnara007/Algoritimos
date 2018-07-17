def kadane(lista):
	
	maxAtual = 0
	maxTotal = 0
	
	for elemento in lista:
		
		maxAtual = max(maxAtual + elemento, elemento)
		maxTotal = max(maxTotal, maxAtual)
		
		if maxTotal < 0: 
			
			maxTotal = 1
	
	return maxTotal

lista = map(int, raw_input().split())

print kadane(lista)
