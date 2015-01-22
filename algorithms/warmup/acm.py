# Enter your code here. Read input from STDIN. Print output to STDOUT

N,M = raw_input().split(" ")
N = int(N)
M = int(M)

p = []

for i in range(N):
	p.append(int(raw_input(), 2))

max = 0
nMax = 0
for i in range(0,N-1):
	for j in range(i+1,N):
		#print bin(p[i]), bin(p[j]), bin(p[i] | p[j])
		#v = eval("+".join([n for n in (bin(p[i] | p[j])[2:]).zfill(M)]))
		v = bin(p[i] | p[j]).count('1')
		if v > max:
			max = v
			nMax = 1
		elif v == max:
			nMax += 1

print max
print nMax