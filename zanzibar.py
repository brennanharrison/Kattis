#!/usr/bin/env python
# coding: utf-8

# In[2]:


def test(l):
    ol = []
    p = 1
    for i in l[:-1]:
        if l[p] > (i+i):
            a = l[p] - (i+i)
            ol.append(a)
        else:
            a = 0
            ol.append(a)
        p+=1
    z = sum(ol)
    pl.append(z)


n = int(input())

x = 0

pl = []

while x < n:
    u = [int(x) for x in input().split()]
    test(u)
    x+=1
    
for i in pl:
    print(i)

