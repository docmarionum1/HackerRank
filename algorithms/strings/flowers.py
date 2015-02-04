#!/bin/python

N, K = map(int, raw_input().split())
prices = map(int, raw_input().split())
prices.sort()
people = [0]*K
total = 0
person = 0

while prices:
    p = prices.pop()
    total += p*(1+people[person])
    people[person] += 1
    person = (person + 1) % K

print total