# Enter your code here. Read input from STDIN. Print output to STDOUT
from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction

C_memo = {}
Q_memo = {}

def C(n,k):
    key = str(n)+","+str(k)
    if key in C_memo:
        return C_memo[key]
    else:
        v = int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )
        C_memo[key] = v
        return v

def Q(N,K):
    key = str(N)+","+str(K)
    if key in Q_memo:
        return Q_memo[key]
    else:
        s = 0
        for i in range(1,K+1):
            c = C(N,i)
            if (K-i) > 0:
                c = c *Q(i, K-i)
                s += c
            else:
                s += c
            print N, K, i, c
        s = s % (10**9)        
        Q_memo[key] = s    
        return s


for _ in range(int(raw_input())):
    N = int(raw_input())
    K = int(raw_input())
    print Q(N,K) 
    exit()