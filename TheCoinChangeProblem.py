#The Coin Change Problem
#Tags: Dynamic Programming, Memoization
#https://www.hackerrank.com/challenges/coin-change/problem

from math import *
A,b = map(int,raw_input().split())
B = map(int,raw_input().split())
coins = {}

for i in range(1,len(B)+1):
    coins[i] = B[i-1]
if A == 0:
    print '1'
    exit()
if A > 0 and b == 0:
    print '0'
    exit()
ways = {}
ways[0] = 1
for i in xrange(1,A+1):
    ways[i] = 0

for i in xrange(1,len(B)+1):
    for j in xrange(coins[i],A+1):
        ways[j] = ways[j] + ways[j-coins[i]]

print ways[A]