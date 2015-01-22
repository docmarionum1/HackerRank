# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

n = int(raw_input())

squares = [i*i for i in range(int(math.ceil(math.sqrt(10**9))))]

for i in range(n):
    a,b = [int(j) for j in raw_input().split(' ')]
    low = math.ceil(math.sqrt(a))**2
    if low in squares:
        start = squares.index(low)
    else:
        start = len(squares)
    
    high = math.floor(math.sqrt(b))**2
    if high in squares:
        end = squares.index(high)
    else:
        end = len(squares) - 1
        
    print end - start + 1