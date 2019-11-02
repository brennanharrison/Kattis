#!/usr/bin/env python
# coding: utf-8

# In[5]:


ol = []

while True:
    u = [float(x) for x in input().split()]
    if u[0] == 0:
        break
    x1 = u[0]
    y1 = u[1]
    x2 = u[2]
    y2 = u[3]
    p = u[4]
    e = 1/p
    q = abs(x1-x2)**p
    r = abs(y1-y2)**p
    n = round((q+r)**e,10)
    ol.append(n)
    
for i in ol:
    print(i)

