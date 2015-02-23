#http://community.topcoder.com/stat?c=problem_statement&pm=11278

def getUnsorted(l):
    if len(l) < 2:
        return []
        
    l.sort()
    
    j = len(l) - 1 
    while j > 0 and l[j] == l[j-1]:
        j -= 1
        
    if j == 0:
        return []
        
    t = l[j]
    l[j] = l[j-1]
    l[j-1] = t
    
    return l
    
    
getUnsorted([2,8,5,1,10,5,9,9,3,10,5,6,6,2,8,2,10]) #[1, 2, 2, 2, 3, 5, 5, 5, 6, 6, 8, 8, 9, 10, 9, 10, 10]