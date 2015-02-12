# Enter your code here. Read input from STDIN. Print output to STDOUT

def minish(c, s):
    for c2 in sorted(s):
        if c2 > c:
            return c2

for _ in range(int(raw_input())):
    w = raw_input().strip()
    ans = None
    for i in range(len(w)-2, -1, -1):
        end = w[i+1:]
        m = minish(w[i], end)
        if m > w[i]:
            end = end.replace(m, w[i], 1)
            ans = w[:i] + m + "".join(sorted(end))
            break
    print "no answer" if ans is None else ans