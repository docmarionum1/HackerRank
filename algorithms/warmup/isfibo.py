fib = [1]

def gen_fib():
    #global fib
    a = 1
    b = 1
    while True:
        c = a + b
        a = b
        b = c
        fib.append(c)
        yield c
    

T = int(raw_input())

for i in range(T):
    n = int(raw_input())
    g = gen_fib()
    while n > fib[-1]:
        next(g)
    print "IsFibo" if n in fib else "IsNotFibo"