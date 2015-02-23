#http://community.topcoder.com/stat?c=problem_statement&pm=10509

import string

def encrypt(s):
    cmap = list(string.ascii_uppercase)
    for i in range(len(s)):
        if not s[i].isupper():
            s = s.replace(s[i], cmap.pop(0))
    return s.lower()
    
encrypt('encryption') #'abcdefghib'