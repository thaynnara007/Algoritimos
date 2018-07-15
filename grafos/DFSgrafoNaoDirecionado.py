visitados = [False] * 100001
listaAdjacencia = [0] * 100001

def DFS(no):
	
	global visitados
	global listaAdjacencia
	
	visitados[no] = True
	
	for filho in listaAdjacencia[no]:
		
		if not visitados[filho]:
			
			dfs(filho)
		
		
	
	
	
