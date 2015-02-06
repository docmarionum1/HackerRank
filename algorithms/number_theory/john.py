# Enter your code here. Read input from STDIN. Print output to STDOUT
from fractions import gcd

for _ in range(int(raw_input())):
    N = int(raw_input())
    A = map(int, raw_input().split())
    B = [A[0]] + [-1]*(N-1) + [A[-1]]
    for i in range(1,N):
        if A[i] % A[i-1] == 0:
            B[i] = A[i]
        elif A[i-1] % A[i] == 0:
            B[i] = A[i-1]
        else:
            mi = min(A[i], A[i-1])
            ma = max(A[i], A[i-1])
            for j in range(1,mi+1):
                if (ma*j)%mi == 0:
                    B[i] = ma*j
                    break
        
    print " ".join(map(str, B))