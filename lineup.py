#!/usr/bin/env python
# coding: utf-8

# In[11]:


n= int(input())

x = 0

oL = []

while x < n:
    u = input()
    oL.append(u)
    x+=1
    
oLSort = oL[:]
oLSort.sort()
oLReverse = oLSort[:]
oLReverse.reverse()


if oL == oLSort:
    print('INCREASING')
elif oL == oLReverse:
    print('DECREASING')
else:
    print('NEITHER')

