#Hardest 5 points ever.

from fractions import Fraction

for _ in range(int(raw_input())):
    A,B,C = map(int, raw_input().split())
    
    if C > A + B:
        N = 1
        D = 1
    elif C <= A and C <= B:
        N = C**2
        D = A*B*2
    elif C >= A and C >= B:
        N = 2*A*B - (A+B-C)*(B-C+A)
        D = 2*A*B
    else:
        B,A = sorted([A,B])
        N = 2*A*B - 2*B*(A-C) - B**2
        D = 2*A*B
        
    if N == D:
        print "1/1"
    else:
        print Fraction(N, D)