#!/usr/bin/env python
# coding: utf-8

# In[8]:


n =int(input())

l = [int(x) for x in input().split()]

o = [int(x) for x in l if x < 0]

if o == []:
    print(str(0))
else:
    print(abs(sum(o)))

