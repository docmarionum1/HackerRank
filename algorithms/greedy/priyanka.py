N = int(raw_input())
W = map(int, raw_input().split())
W.sort(reverse=True)
    
buys = 0

while len(W) > 0:
    i = W[-1]
    
    while W and W[-1] < i + 5:
        W.pop()
        
    buys += 1
    
print buys