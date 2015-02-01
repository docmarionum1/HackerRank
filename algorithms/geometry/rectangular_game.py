# Enter your code here. Read input from STDIN. Print output to STDOUT
   board.append(array.array('I',[0]*m))

minA = 10**6
minB = 10**6

for _ in range(int(raw_input())):
    a,b = map(int, raw_input().split())

    if a < minA:
        minA = a
    if b < minB:
        minB = b

print minA * minB