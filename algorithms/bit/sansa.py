# If length of array is even it's always 0
# Otherwise it's the XOR of every other element
from operator import xor


# Version 1
T = int(raw_input())

for _ in range(T):
    raw_input()
    a = map(int, raw_input().split())
    if len(a) % 2 == 0:
        print 0
    else:
        print reduce(xor, [a[i] for i in range(0,len(a),2)])

# Version 2
for _ in range(int(raw_input())):
    if int(raw_input()) % 2:
        print reduce(xor, map(int, raw_input().split()[::2]))
    else:
        print 0
        raw_input()
        
# Version 3, one liner
print "\n".join(str(reduce(xor, map(int, raw_input().split()[::2]) if int(raw_input())%2 else [0] if raw_input() else [0])) for i in range(int(raw_input())))

