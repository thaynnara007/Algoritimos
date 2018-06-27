WHITE = 0
GREY = 1
BLACK = 2

def dfs(no):
	
	global loop
	global visitados
	global listaAdjacencia
	global WHITE
	global GREY
	global BLACK
	
	visitados[no] = GREY
	
	if loop : return 
	
	if listaAdjacencia[no] != 0:
		
		for filho in listaAdjacencia[no]:
			
			if visitados[filho] == WHITE:
				
				dfs(filho)
			
			elif visitados[filho] == GREY:
				
				loop = True
				return 
	
	visitados[no] = BLACK

#algoritimo para rodar toda a dfs no grafo
def rodaGrafo():
	
	global loop
	global nos
	
	for no in nos:
		
		if loop : break
		
		if visitados[no] == WHITE:
			
			dfs(no)
			
			if loop : break
	
	return loop

t = int(raw_input())
#ler grafo
for i in xrange(t):
	
	loop = False
	listaAdjacencia = [0] * 10001
	visitados = [WHITE] * 10001
	nos = set([])
	
	_, arestas = map(int, raw_input().split())
	
	for j in xrange(arestas):
		
		no1, no2 = map(int, raw_input().split())
		
		nos.add(no1)
		nos.add(no2)
		
		if listaAdjacencia[no1] != 0:
			
			listaAdjacencia[no1].append(no2)
		
		else:
			
			listaAdjacencia[no1] = [no2]
