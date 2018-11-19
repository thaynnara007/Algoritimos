def numeroBinomial(n,k):

    global dp

    for i in xrange(1, n + 1):
        for j in xrange(k + 1):

            if j == 0: dp[i][j] = 1
            elif j == i: dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][ j - 1] + dp[i - 1][ j]

    return dp[n][k]



n = int(raw_input("numero de intens:"))
k = int(raw_input("numero de opcoes de escolha:"))
dp = [[0 for i in xrange(k + 1)] for j in xrange(n + 1)]

print numeroBinomial(n,k)


