import math
s,a=lambda x,n:sum(x**(i*2+n)/math.factorial(i*2+n)*[1,-1][i%2] for i in range(5)),input
for _ in[0]*a():
	x=a()
	print s(x,1),'\n',s(x,0)