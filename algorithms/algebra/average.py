def S(l):
    while len(l) > 1:
        a = l[0]
        b = l[1]
        l[0] = a + b + a*b
        l.pop(1)
    return l[0] % 1000000007

raw_input()
a = map(int, raw_input().split())
print S(a)