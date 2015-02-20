#http://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493

def longestZigZag(l):
    d = []
    for i in range(1,len(l)):
        d.append(l[i] - l[i-1])
    i = 1
    while i < len(d):
        if d[i]/d[i-1] >= 0:
            d = d[:i] + d[i+1:]
        else:
            i += 1
    print len(d)+1
    

longestZigZag([
374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
249, 22, 176, 279, 23, 22, 617, 462, 459, 244
]) #36