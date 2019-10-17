#!/usr/bin/env python
# coding: utf-8

# In[3]:


n, q = [int(x) for x in input().split()]

l = [int(x) for x in input().split()]

output = []

x = 0

while x < q:
    a,b,c = [int(x) for x in input().split()]
    if a == 1:
        l[b-1] = c
    else:
        y = abs(l[b-1]-l[c-1])
        output.append(y)
    x+=1
    
for i in output:
    print(i)

