import math

'''
This is just whether X is a number in the series 1+2+3...

X = N^2 + N
    -------
       2
       
Which equals the quadratic equation

0 = N^2 + N - 2X

So using the quadratic formula:

N = (-1 + sqrt(1 - 8X))/2
'''

for _ in range(int(raw_input())):
    n = int(raw_input())
    s = math.sqrt(1 + 8*n)
    if not s.is_integer():
        print "Better Luck Next Time"
    else:
        print "Go On Bob", int((s-1)/2)