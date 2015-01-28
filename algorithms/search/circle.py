from math import sqrt, ceil

for _ in range(int(raw_input())):
    r,k = map(int, raw_input().split())
    c = 1 if sqrt(r).is_integer() else 0
        
    for x in range(1,int(ceil(sqrt(r)))):
        if sqrt(r - x**2).is_integer():
            c += 1
    
    print "possible" if 4*c <= k else "impossible"