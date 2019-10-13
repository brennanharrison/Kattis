#!/usr/bin/env python
# coding: utf-8

# In[7]:


x, y = [int(x) for x in input().split()]

if x == 0 and y ==0:
    print('Not a moose')
elif x > y:
    print('Odd', x+x)
elif x < y:
    print('Odd', y+y)
else:
    print('Even', x+y)

