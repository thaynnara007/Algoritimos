def troco(valor, sizeMoedas):

    global dp
    global moedas

    for i in xrange(2, sizeMoedas + 1):
        for j in xrange(1, valor + 1):
           
            if moedas[i - 1] > j: dp[i][j] = dp[i - 1][j]
            else: dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - moedas[i - 1]])

    return dp[-1][-1]

def findMoedas(qntdMoedas, valor, sizeMoedas):

    global dp
    global moedas
    i = sizeMoedas
    j = valor
    moedasPegas = []

    while qntdMoedas > 0:

        v1 = dp[i - 1][j]
        v2 = 1 + dp[i][j - moedas[i - 1]]

        if dp[i][j] == v1: i -= 1
        else: 
            moedasPegas.append(moedas[i - 1])
            j -= moedas[i - 1]
            qntdMoedas -= 1
    
    print moedasPegas
        
moedas = map(int, raw_input("moedas:").split())
valor = int(raw_input("valor:"))
sizeMoedas = len(moedas)
dp = [[0 for i in xrange(valor + 1)] for j in xrange(sizeMoedas + 1)]

for j in xrange(valor + 1):
    dp[1][j] = j

qntdMoedas = troco(valor, sizeMoedas)
findMoedas(qntdMoedas, valor, sizeMoedas)