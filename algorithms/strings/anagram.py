from string import ascii_lowercase as alph

for _ in range(int(raw_input())):
    s = list(raw_input())
    if len(s) % 2 == 1:
        print -1
        continue
        
    s1 = s[:len(s)/2]
    s2 = s[len(s)/2:]

    d = dict([(c,0) for c in alph])
    
    for c in s1:
        d[c] += 1
        
    for c in s2:
        d[c] -= 1
        
    print sum([abs(i) for i in d.values()])/2