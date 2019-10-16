#!/usr/bin/env python
# coding: utf-8

# In[19]:


import collections


n = int(input())

q = 0

d = {}

while q < n:
    x,y = [str(x) for x in input().split()]
    if x.isnumeric():
        x = int(x)
        x = x/2
        d[x] = y
    else:
        y = int(y)
        y = y/1
        d[y] = x
    q+=1


od = collections.OrderedDict(sorted(d.items()))

for k, v in od.items():
    print(v)

