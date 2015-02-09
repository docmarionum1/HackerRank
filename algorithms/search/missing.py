from sets import Set

n = int(raw_input())
A = map(int, raw_input().split())
m = int(raw_input())
B = map(int, raw_input().split())
A.sort()
B.sort()
diff = []
i = 0
j = 0
while j < len(B):
    if i < len(A) and A[i] == B[j]:
        i += 1
        j += 1
    else:
        diff.append(B[j])
        j += 1   
        
print " ".join(map(str, sorted(Set(diff))))