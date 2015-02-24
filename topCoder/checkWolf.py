#http://community.topcoder.com/stat?c=problem_statement&pm=12778

def checkWolf(s):
    i = 0
    while i < len(s):
        if s[i] is not 'w':
            return "INVALID"
            
        count = 0
        while s[i] == 'w':
            count += 1
            i += 1
        for c in ['o','l','f']:
            for j in range(count):
                if s[i] is not c:
                    return "INVALID"
                i += 1
    return "VALID"
    
checkWolf("wolfwwoollffwwwooolllfffwwwwoooollllffff") #VALID
checkWolf("wwolfolf") #INVALID