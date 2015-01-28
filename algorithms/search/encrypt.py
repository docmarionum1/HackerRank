# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt, floor, ceil
s = raw_input()
rows = int(sqrt(len(s)))
cols = int(ceil(sqrt(len(s))))
print " ".join([s[i::cols] for i in range(rows if cols == rows else rows+1)])