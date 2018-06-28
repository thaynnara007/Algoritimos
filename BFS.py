import Queue

listaAdjacencia [0] * 100001
visitados = [False] * 100001

def BFS(no):
	
	global listaAdjacencia
	global visitados
	
	fila = Queue.Queue()
	visitados[no] = True
	fila.put(no)
	
	while not fila.empty():
		
		noAtual = fila.get()
		
		for filho in listaAdjacencia[no]:
			
			if not visitados[filho]:
				
				visitados[filho] = True
				fila.put(filho)
