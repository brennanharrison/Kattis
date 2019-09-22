#!/usr/bin/env python
# coding: utf-8

# In[18]:


n = int(input())

l = list(map(int,input().split()))

p = []

q = []

while True:
    p.append(l[0])
    n = 0
    for i in l:
        if i > p[n]:
            p.append(i)
            n+=1
    break
    
for i in p:
    q.append(str(i))
    
print(len(p))
print(' '.join(q))

