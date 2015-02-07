# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, rupees):
  prices.sort()
  answer = 0
  while rupees > prices[0]:
    v = prices.pop(0)
    answer += 1
    rupees -= v
  
  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)