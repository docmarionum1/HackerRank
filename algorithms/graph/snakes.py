ladders = None
snakes = None
snake_mouths = None

def shortestPath(start, end):
    for i,j in ladders:
        if i >= start and j <= end:
            return shortestPath(start, i) + shortestPath(j, end)
    
    rolls = 0
    loc = start
    while loc < end:
        for i in range(6, 0, -1):
            j = loc + i
            if j <= end and j not in snake_mouths:
                break
        rolls += 1
        loc = j
        
    return rolls
        
for _ in range(int(raw_input())):
    L,S = map(int, raw_input().split(","))
    ladders = [map(int, x.split(",")) for x in raw_input().split()]
    snakes = [map(int, x.split(",")) for x in raw_input().split()]
    snake_mouths = map(lambda s: s[0], snakes)
    ladders = sorted(ladders, key=lambda l: l[1]-l[0])[::-1]
    print shortestPath(1,100)