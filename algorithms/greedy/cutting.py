for _ in range(int(raw_input())):
    M,N = map(int, raw_input().split())
    y = sorted(map(int, raw_input().split()))
    x = sorted(map(int, raw_input().split()))
    
    y_pieces = 1
    x_pieces = 1
    cost = 0
    
    while y or x:
        if not y or (x and x[-1] >= y[-1]):
            cost += x.pop() * x_pieces
            y_pieces += 1
        else:
            cost += y.pop() * y_pieces
            x_pieces += 1
            
    print cost % (10**9 + 7)