def buscaBinaria(procurado, lista, inicio, fim):
	
	while (inicio <= fim):

		meio = (inicio + fim) / 2

		e = lista[meio]
		
		if e < procurado:
			
			inicio = meio + 1
		
		elif e > procurado:
			
			fim = meio - 1
		
		else:
			
			return meio

	return inicio
