s = "ABABABAB"
count = 0

while True:
	for c in ["AA", "BB"]:
		t = s.split(c)
		count += (len(t)-1)
		s = c[0].join(t)
	if "AA" not in s and "BB" not in s:
		break
            
print count