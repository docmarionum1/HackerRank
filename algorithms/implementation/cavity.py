# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
map = []
for i in range(n):
    map.append(raw_input())
    
print map[0]

if n > 2:
    for i in range(1,n-1):
        #new_map.append(map[i])
        s = map[i][0]
        for j in range(1,n-1):
            if map[i][j] > map[i-1][j] and map[i][j] > map[i][j-1] and map[i][j] > map[i+1][j] and map[i][j] > map[i][j+1]:
                s = s + "X"
            else:
                s = s + map[i][j]
        s = s + map[i][n-1]
        print s

if n > 1:
    print map[n-1]