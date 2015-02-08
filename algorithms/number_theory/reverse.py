for _ in range(int(raw_input())):
    N, K = map(int, raw_input().split())
    if K < N/2:
        print 2*K+1
    else:
        print int(2*(K - 2*(K-(N-1.0)/2)))