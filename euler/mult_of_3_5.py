# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
memo = {0:0}
last = 0
order = []

i = 0
while i < T:
    i += 1
    n = int(raw_input())
    order.append(n)
    
sorted_T = sorted(order)

for n in sorted_T:    
    if n in memo:
        continue
    
    j = last
    j3 = j if j % 3 == 0 else (j+3)/3*3
    j5 = j if j % 5 == 0 else (j+5)/5*5
    j15 = j if j % 15 == 0 else (j+15)/15*15

    s = memo[last] + sum(xrange(j3,n,3)) + sum(xrange(j5,n,5)) - sum(xrange(j15,n,15))
        
    memo[n] = s
    last = n
    
for i in order:
    print memo[i]