# Enter your code here. Read input from STDIN. Print output to STDOUT
p = 10**9 + 7

N, M = map(int, raw_input().split())
A = [None] + map(int, raw_input().split())
B = map(int, raw_input().split())
C = map(int, raw_input().split())
BC = {}

for i in xrange(M):
    BC[B[i]] = 1

for i in xrange(M):
    BC[B[i]] = BC[B[i]] * C[i] % p

for k,v in BC.iteritems():
    for i in xrange(k,N+1,k):
        A[i] = A[i] * v % p
        
A.pop(0)
print " ".join(map(str, A))