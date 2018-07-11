
def getParent(no):
	
	global parents
	
	if no == parents[no]: return parents[no]
	else:
		
		parents[no] = getParent(parents[no])
		
		return parents[no]

def union(no1, no2):
	
	global parents
	
	no1Parent = getParent(no1)
	no2Parent = getParent(no2)
	
	parents[no2Parent] = no1Parent

def isSameSet(no1, no2):
	
	return getParent(no1) == getParent(no2)

nos, qntdArestas = map(int, raw_input().split())
parents = [i for i in xrange(501)]
arestas = []

for aresta in xrange(qntdArestas):
	
	no1, no2, peso = map(int, raw_input().split())
	
	arestas.append((peso, no1,no2))

arestas.sort()
tamanho = 0
for aresta in arestas:

	peso = aresta[0]
	no1 = aresta[1]
	no2 = aresta[2]

	if not isSameSet(no1, no2):
	
		union(no1,no2)
		tamanho += peso

print tamanho
