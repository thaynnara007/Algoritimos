def knapsack():
	
	global dp
	global itens
	global qntdItens
	global capacidadeTotal
	
	for item in xrange(1, qntdItens + 1):
		
		for capacidade in xrange(1, capacidadeTotal + 1):
			
			#item = (valor, peso)
			if itens[item][1] > capacidade: 
				
				dp[item][capacidade] = dp[item - 1][capacidade]
			
			else:
				
				#maximo entre pegar ou nao pegar o item
				dp[item][capacidade] = max(dp[item - 1][capacidade], dp[item - 1][capacidade - itens[item][1]] + itens[item][0])

VALOR = 0
PESO = 1
def findItens(qntdItens, capacidadeTotal, valorMaximo):

	global itens
	global dp
	item = qntdItens
	capacidade = capacidadeTotal
	itensPegos = []

	while valorMaximo > 0:

		v1 = dp[item - 1][capacidade]
		v2 = dp[item - 1][capacidade - itens[item][PESO]] + itens[item][VALOR]
	
		if v1 == dp[item][capacidade]: item -= 1
		else:
			itensPegos.append(item)
			valorMaximo -= itens[item][VALOR]
			capacidade -= itens[item][PESO]
			item -=1 
	
	return itensPegos


#ler entrada
qntdItens = int(raw_input("Quantidade de itens:"))
capacidadeTotal = int(raw_input('capacidade mochila:'))

#cria a matriz
dp = [[0 for i in xrange(capacidadeTotal + 1)] for j in xrange(qntdItens + 1)]
itens = [0] * (qntdItens + 1)
#caso base
itens[0] = (0,0)

print "valor peso"
for item in xrange(1,qntdItens + 1):
	
	valor, peso = map(int, raw_input().split())
	itens[item] = (valor, peso)

knapsack()
valorMaximo = dp[-1][-1]
print findItens(qntdItens, capacidadeTotal, valorMaximo)
	
