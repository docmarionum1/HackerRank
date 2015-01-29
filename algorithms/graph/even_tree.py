# Enter your code here. Read input from STDIN. Print output to STDOUT

def size(i,j):
    count = 1
    visited = [i]
    s = [n for n in tree[i] if n != j]
    while s:
        count += 1
        n = s.pop()
        visited.append(n)
        
        for e in tree[n]:
            if e not in visited:
                s.append(e)
                
    return count

n,m = map(int, raw_input().split())
tree = [None]*(n+1)
edges = []
for i in range(m):
    v,e = map(int, raw_input().split())
    edges.append((v,e))
    if tree[v]:
        tree[v].append(e)
    else:
        tree[v] = [e]
        
    if tree[e]:
        tree[e].append(v)
    else:
        tree[e] = [v]

count = 0
for i,j in edges:
    if size(i,j) % 2 == 0:
        count += 1
        tree[i].remove(j)
        tree[j].remove(i)
        
print count