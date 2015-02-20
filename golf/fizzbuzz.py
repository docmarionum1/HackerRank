for i in range(1,101):print(''if i%3 else'Fizz')+(''if i%5 else'Buzz')or i
for i in range(100):print'Fizz'*(i%3/2)+'Buzz'*(i%5/4)or i+1