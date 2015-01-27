# Enter your code here. Read input from STDIN. Print output to STDOUT

def RCR(A,K):
    
    for i in range(K%len(A)):
        A = [A.pop()] + A
    return A


N,K,Q = map(int, raw_input().split())
A = map(int, raw_input().split())

if Q > K%N:
    A = RCR(A,K)
    for _ in range(Q):
        print A[int(raw_input())]
else:
    j = K%N
    for _ in range(Q):
        i = (int(raw_input()) - K)%N
        print A[i]