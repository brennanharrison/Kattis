#!/usr/bin/env python
# coding: utf-8

# In[6]:


def getPassengers(stops):
    u = 1
    n = 0
    while (u <= stops):
        n = n + (n + 0.5) + 0.5
        u+=1
    return n



t = int(input())

p = [] 
h = 1

while (h <= t):
    k = int(input())
    l = getPassengers(k)
    p.append(l)
    h+=1
    
for i in p:
    print(int(i))

