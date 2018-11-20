def LCS(sequencia1, size1, sequencia2, size2):

    global dp

    for i in xrange(1, size1 + 1):
        for j in xrange(1, size2 + 1):

            if sequencia1[i - 1] == sequencia2[j - 1]: dp[i][j] = 1 + dp[i - 1][j - 1]
            else: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[-1][-1]

def findSubsquence(sequencia1, size1, sequencia2, size2, n):

    i = size1
    j = size2
    subsequence = ""

    while n > 0:

        if sequencia1[i - 1] == sequencia2[j - 1]: 
            
            subsequence = sequencia1[i - 1] + subsequence
            i -= 1
            j -= 1
            n -= 1
        
        else:
            v1 = dp[i - 1][j]
            v2 = dp[i][j - 1]

            if dp[i][j] == v1: i -= 1
            else: j -= 1
    
    return subsequence


sequencia1 = raw_input("Sequencia1:")
sequencia2 = raw_input("Sequencia2:")
size1 = len(sequencia1)
size2 = len(sequencia2)
dp = [[0 for j in xrange(size2 + 1)] for i in xrange(size1 + 1)]

n = LCS(sequencia1, size1, sequencia2, size2)
print findSubsquence(sequencia1, size1, sequencia2, size2, n)




