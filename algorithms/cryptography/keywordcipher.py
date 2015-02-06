# Enter your code here. Read input from STDIN. Print output to STDOUT'
from collections import OrderedDict
from string import ascii_uppercase

for _ in range(int(raw_input())):
    key = raw_input()
    text = raw_input()
    key = "".join(OrderedDict.fromkeys(key)) #Remove duplicates
    order = [key.find(c) for c in ascii_uppercase if key.find(c) != -1]
    a = "".join([i for i in ascii_uppercase if i not in key])
    m = key + a
    m2 = "".join(m[i::len(key)] for i in order)
    s = dict(zip(m2, ascii_uppercase))
    s[" "] = " "
    print "".join(s[t] for t in text)