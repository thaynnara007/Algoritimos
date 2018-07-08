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
				

#ler entrada
qntdItens = int(raw_input())
capacidadeTotal = int(raw_input())

#cria a matriz
dp = [[0 for i in xrange(capacidadeTotal + 1)] for j in xrange(qntdItens + 1)]
itens = [0] * (qntdItens + 1)
#caso base
itens[0] = (0,0)

for item in xrange(1,qntdItens + 1):
	
	valor, peso = map(int, raw_input().split())
	itens[item] = (valor, peso)

knapsack()
print dp[-1][-1]
	
