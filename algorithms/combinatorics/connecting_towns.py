from operator import mul

for _ in range(int(raw_input())):
    raw_input()
    print reduce(mul, map(int, raw_input().split())) % 1234567