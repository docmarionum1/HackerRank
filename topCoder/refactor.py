#http://community.topcoder.com/stat?c=problem_statement&pm=2986&rd=5862
import math

memo = {}

def refactor(n):
    if n in memo:
        return memo[n]

    factors = []
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:    
            a = [[i]] + [map(int, q.split("*")) for q in refactor(i)]
            b = [[n/i]] + [map(int, q.split("*")) for q in refactor(n/i)]
            for x in a:
                for y in b:
                    f = "*".join(map(str, sorted(x + y)))
                    if f not in factors:
                        factors.append(f)
    memo[n] = factors
    return factors

print len(refactor(24)) #6
print len(refactor(9973)) #0
print len(refactor(9240)) #295