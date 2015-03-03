import math

preprimes = [6]

def isPreprime(n):
    count = 2
    for i in range(2, int(n/2)+1):
        if n%i == 0:
            count += 1
            if count > 4:
                return False
                
    if count == 4:
        return True
    
    return False
    
def nthNumber(n):
    if n <= len(preprimes):
        return preprimes[n-1]
    else:
        start = preprimes[-1] + 1
        while len(preprimes) < n:
            if isPreprime(start):
                preprimes.append(start)
            start += 1
        return preprimes[-1]