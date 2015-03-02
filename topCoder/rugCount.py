import math

def rugCount(area):
	dims = []
	for i in range(1, int(math.sqrt(area)+1)):
		if area % i == 0:
			a = i
			b = area/i
			if a % 2 == 0 and b % 2 == 0 and a != b:
				continue
			a,b = sorted([a,b])
			m = str(a) + "*" + str(b)
			if m not in dims:
				dims.append(m)

	return dims

print len(rugCount(4)) #2
print len(rugCount(8)) #1