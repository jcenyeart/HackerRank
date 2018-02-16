#Balanced Brackets
#Tags: Pop/Queue
https://www.hackerrank.com/challenges/balanced-brackets/problem

import sys
### TRY USING STACKS
parentdict2 = {}
parentdict2['['] = ']'
parentdict2['('] = ')'
parentdict2['{'] = '}'
leftps = ['[','(','{']

#Add each bracket one by one.  If valid closure, remove the pair and continue.

def validPs(s):
    l = []
    for i in range(0,len(s)):
        if l:
            if s[i] in leftps:
                l.append(s[i])
                continue
            elif parentdict2[l[-1]] == s[i]:
                l.pop()
                continue
            else:
                return False
        elif s[i] in leftps:
            l.append(s[i])
        else:
            return False
    if l:
        return False
    else:
        return True

t = int(raw_input().strip())
for a0 in xrange(t):
    s = raw_input().strip()
    if validPs(s):
        print 'YES'
    else:
        print 'NO'
