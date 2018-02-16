#Strings:Making Anagrams
#Tags:None
#https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

a = list(raw_input().strip())
b = list(raw_input().strip())
c = []
for i in xrange(len(a)):
    if a[i] in b:
        c.append(a[i])
        b.remove(a[i])
for ele in c:
    a.remove(ele)
print len(a)+len(b)