for _ in range(int(raw_input())):
    r = int(raw_input())
    if r < 3:
        print -1
    elif r % 2 == 1:
        print 2
    elif (r-2) % 4 == 0:
        print 4
    else:
        print 3