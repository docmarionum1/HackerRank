#http://community.topcoder.com/stat?c=problem_statement&pm=8171

def sortSerials(a):
    a.sort()
    a.sort(key=lambda s: sum(int(d) for d in s if d.isdigit()))
    a.sort(key=lambda s: len(s))
    return a