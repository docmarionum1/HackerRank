#from random import shuffle
import random



n,a,b = map(int, raw_input().split())
arr = map(int, raw_input().split())

total = sum(arr)
arr2 = []

x = ((n - 2)/n)**a

const = 1./n + 1./(n-1)
const2 = 1 - const
const3 = const/(n-1)

const2a = const2**a
const3a = const3**a

def simSwap(v,o,n,c):
    if c == 0:
        return v
    
    return const2 * simSwap(v, o, n, c-1) + const3*o

for i in range(n):
    arr2.append(simSwap(arr[i], total - arr[i], n, 17))#a - n/2*b))
    #arr2.append(const2a*arr[i]**a + const3a*(total-arr[i])**a)

print arr
print arr2
#exit()
#random.shuffle(a)
s = 0
count = 0.0
for i in range(n):
    for j in range(i+2,n+1):
        #print a[i:j]
        s += sum(arr2[i:j])
        count += 1.0
        
print s/count