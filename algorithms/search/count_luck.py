# Enter your code here. Read input from STDIN. Print output to STDOUT

def pathfind(grid, n, m, start, end):
    if start == end:
        return []
    
    neighbors = [
        (start[0]-1, start[1]),
        (start[0]+1, start[1]),
        (start[0], start[1]-1),
        (start[0], start[1]+1),
    ]
    
    grid[start[1]][start[0]] = 'V'
    
    for i,j in neighbors:
        if i >= 0 and i < m and j >= 0 and j < n and grid[j][i] in [".", "*"]:
            p = pathfind(grid, n, m, (i,j), end)
            if p is not None:
                p.append((i,j))
                return p
            
    return None

def countIntersections(grid, n, m, path, threshold):
    if not path:
        return 0
    
    start = path[0]
    
    neighbors = [
        (start[0]-1, start[1]),
        (start[0]+1, start[1]),
        (start[0], start[1]-1),
        (start[0], start[1]+1),
    ]
    
    count = 0
    
    for i,j in neighbors:
        if i >= 0 and i < m and j >= 0 and j < n and grid[j][i] in [".", "*", "V"]:
            count += 1
            
    inter = 1 if count >= threshold else 0
    
    threshold = 3
    
    return inter + countIntersections(grid, n, m, path[1:], threshold)
    
    
for _ in range(int(raw_input())):
    N,M = map(int, raw_input().split())
    grid = []
    start = None
    end = None
    
    for i in range(N):
        row = list(raw_input())
        if "*" in row:
            end = (row.index("*"), i)
        if "M" in row:
            start = (row.index("M"), i)
        grid.append(row)
        
    K = int(raw_input())
        
    path = pathfind(grid, N, M, start, end)
    path.append(start)
    k = countIntersections(grid, N, M, path[:0:-1], 2)
    print "Impressed" if k == K else "Oops!"