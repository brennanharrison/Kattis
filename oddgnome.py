#!/usr/bin/env python
# coding: utf-8

# In[4]:


ol = []
x = 0
o = 1

n = int(input())

while x < n:
    y = [int(x) for x in input().split()]
    u = y[1]
    for i in y[1:]:
        if i != u:
            ol.append(o)
            break
        o+=1
        u+=1
    x+=1
    o = 1


for i in ol:
    print(i)

