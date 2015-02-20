#http://community.topcoder.com/stat?c=problem_statement&pm=2829&rd=5072

def minSums(s,i):
    for j in range(len(s), 0, -1):
        x = int(s[:j])
        if x <= i:
            if s[j:] == "" and i-x == 0:
                return 0
            else:
                y = minSums(s[j:], i-x)
                if y > -1:
                    return 1 + y
        else:
            pass
    return -1
    
 minSums("0123456789", 45) #8
 minSums("9230560001", 71) #4