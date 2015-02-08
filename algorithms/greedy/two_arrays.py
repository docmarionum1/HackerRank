for _ in range(int(raw_input())):
    N,K = map(int, raw_input().split())
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())
    A.sort()
    B.sort(reverse=True)
    possible = True
    for i in range(N):
        if A[i] + B[i] < K:
            possible = False
            break
    
    print "YES" if possible else "NO"