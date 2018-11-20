def LCS(sequencia1, size1, sequencia2, size2):

    global dp

    for i in xrange(1, size1 + 1):
        for j in xrange(1, size2 + 1):

            if sequencia1[i - 1] == sequencia2[j - 1]: dp[i][j] = 1 + dp[i - 1][j - 1]
            else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[-1][-1]

sequencia1 = raw_input("Sequencia1:")
sequencia2 = raw_input("Sequencia2:")
size1 = len(sequencia1)
size2 = len(sequencia2)
dp = [[0 for j in xrange(size2 + 1)] for i in xrange(size1 + 1)]

print LCS(sequencia1, size1, sequencia2, size2)




