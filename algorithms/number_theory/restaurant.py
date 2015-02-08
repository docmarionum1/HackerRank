from fractions import gcd
for _ in range(int(raw_input())):
    l,b = map(int, raw_input().split())
    s = gcd(l,b)
    print l/s * b/s