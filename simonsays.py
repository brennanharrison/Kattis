#!/usr/bin/env python
# coding: utf-8

# In[9]:


n = int(input())

ol = []


x = 0

while x < n:
    u = [str(x) for x in input().split()]
    if u[0] == 'Simon' and u[1] == 'says':
        t = ' '.join(u[2:])
        ol.append(t)
    x+=1
    
for i in ol:
    print(i)

