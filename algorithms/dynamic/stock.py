for _ in range(int(raw_input())):
    n = int(raw_input())
    prices = map(int, raw_input().split())
    memo = [0]*(n-1) + [prices[n-1]]
    
    for i in range(n-2,-1,-1):      
        memo[i] = max(prices[i],memo[i+1])

    profit = 0
    shares = 0
    
    for i in range(n):
        if prices[i] < memo[i]:
            shares += 1
            profit -= prices[i]
        else:
            profit += shares * prices[i]
            shares = 0
            
    print profit