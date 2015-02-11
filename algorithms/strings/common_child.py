# Enter your code here. Read input from STDIN. Print output to STDOUT
from string import ascii_uppercase

def seq(a,b,i):
    if i == len(a):
        return [([i],[i])]
    
    #print "A", a
    #print "B", b
    #print i
    #seqs = seq(a, b, i+1)
    #print seqs
    
    found = dict([(c, False) for c in ascii_uppercase])
    #print found
    
    seqs = [([i],[i])]
    
    longest = 0
    
    for i in range(len(a)-1, -1, -1):
        newseqs = []
        
        for sa,sb in seqs:
            loc1 = b[i:sb[0]].rfind(a[i])
            loc2 = a[i:sa[0]].rfind(b[i])
            if loc1 > -1:
                if len(sa) > longest:
                    longest = len(sa)
                    
                newseqs.append((
                    [i] + sa,
                    [i + loc1] + sb
                ))
            if loc2 > -1:
                if len(sa) > longest:
                    longest = len(sa)
                    
                newseqs.append((
                    [i + loc2] + sa,
                    [i] + sb
                ))
                
            #if len(sa) > 1:
            newseqs.append((sa,sb))
        
        if not found[a[i]]:
            loc1 = b[i:].rfind(a[i])
            if loc1 > -1:
                found[a[i]] = True
                newseqs.append((
                    [i],
                    [i + loc1]
                ))
        
        if not found[b[i]]:
            loc2 = a[i:].rfind(b[i])
            if loc2 > -1:
                found[b[i]] = True
                newseqs.append((
                    [i + loc2],
                    [i]
                ))
        #print i, a[i], b[i], newseqs    
        #return newseqs
        seqs = newseqs
        
    return seqs
    
a = raw_input().strip()
b = raw_input().strip()
#print "A", a
#print "B", b
print max(map(lambda x: len(x[0]), seq(a,b,0)))