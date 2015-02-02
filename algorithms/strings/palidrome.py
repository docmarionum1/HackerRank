# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(raw_input())):
    s = raw_input().strip()
    l = len(s)
    idx = None
    for i in range(l/2):
        if s[i] != s[l-i-1]:
            if s[i+1:i+3] == s[l-i-1:l-i-3:-1]:
                idx = i
            else:
                idx = l-i-1
            break
    if idx is None:
        idx = -1
    print idx