def pascal(n):
    line = [1]
    for k in range(n):
        line.append(line[k] * (n-k) / (k+1))
    return map(lambda a: a%(10**9), line)

for _ in range(int(raw_input())):
    print " ".join(map(str, (pascal(int(raw_input())))))