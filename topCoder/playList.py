#http://community.topcoder.com/stat?c=problem_statement&pm=12437

def playList(n):
    return sorted([str(i)+".mp3" for i in range(1,n+1)])[:50]