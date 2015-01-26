def p2(x):
    return x & x -1 == 0

for _ in range(int(raw_input())):
    N = int(raw_input())
    count = -1
    while N > 1:
        if(p2(N)):
            N = N >> 1
        else:
            N -= 2**((N-1) .bit_length() - 1)
        count += 1
    print ["Louise", "Richard"][count%2]