INF = 100000000;

def findJumps():

    global pulos;
    global jumps;
    global sizePulos;

    for i in xrange(sizePulos - 1, -1, -1):
        if(pulos[i] + i) > sizePulos - 1: jumps[i] = 1;
        else:
            minGlobal =  INF
            
            for j in xrange(i, i + pulos[i]):
                minLocal = min(jumps[j], jumps[j + 1])
                minGlobal = min(minLocal, minGlobal)

            jumps[i] = minGlobal + 1
    
    return jumps[0]

pulos = map(int, raw_input().split())
sizePulos = len(pulos);
jumps = [INF for i in xrange(sizePulos)]

print findJumps()
