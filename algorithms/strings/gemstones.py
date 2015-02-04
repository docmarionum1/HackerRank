# Enter your code here. Read input from STDIN. Print output to STDOUT
from string import ascii_lowercase as alph
count = {}
for c in alph:
    count[c] = 0
    
n = int(raw_input())

for i in range(n):
    r = raw_input()
    for c in alph:
        if c in r:
            count[c] += 1
            
            
gem = 0
for c in alph:
    if count[c] == n:
        gem += 1
        
print gem