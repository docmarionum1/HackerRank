# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(raw_input())

sticks = [int(i) for i in raw_input().split(" ")]
sticks.sort()

while sticks:
    print len(sticks)
    cut = sticks[0]
    sticks = [i-cut for i in sticks if i-cut > 0]