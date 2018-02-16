#Candies
#Tags: None
#https://www.hackerrank.com/challenges/candies/problem

a = input()
b = []
c = {}
for _ in xrange(a):
    b.append(input())
for i in xrange(len(b)):
    c[i] = 1   
for i in xrange(len(b)-1):
    if b[i] < b[i+1]:
        c[i+1] = c[i]+1
for i in list(reversed(xrange(len(b)-1))):
    if b[i] > b[i+1]:
        c[i] = max(c[i],c[i+1]+1)
print sum(c.values())