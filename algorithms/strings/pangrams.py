# Enter your code here. Read input from STDIN. Print output to STDOUT
alph = "abcdefghijklmnopqrstuvwxyz"
s = raw_input().lower()
p = True
for c in alph:
    if c not in s:
        p = False
        break
        
print "pangram" if p else "not pangram"