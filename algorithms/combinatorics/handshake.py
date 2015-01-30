def C2(n): #Special case of combinations when r = 2 
    return (n*(n-1)) >> 1

for _ in range(int(raw_input())):
    print C2(int(raw_input()))