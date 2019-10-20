#!/usr/bin/env python
# coding: utf-8

# In[3]:


t = [str(x) for x in input().split()]

if len(t) == len(set(t)):
    print('yes')
else:
    print('no')

