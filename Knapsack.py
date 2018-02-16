#Knapsack
#Tags: Dynamic Programming
#https://www.hackerrank.com/challenges/unbounded-knapsack/problem

a = input()
for _ in xrange(a):
    b,c = map(int,raw_input().split())
    s = list(set(map(int,raw_input().split())))
    def F(n):
        if 1 in s:
            return 0
        if n == 0:
            return 0
        candidates = set()
        for ele in s:
            if ele <= n:
                candidates.add(ele)
        if not candidates:
            return n
        d = min([F(n-ele) for ele in candidates])
        return d
    print c-F(c)