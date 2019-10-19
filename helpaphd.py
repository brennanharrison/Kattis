#!/usr/bin/env python
# coding: utf-8

# In[5]:


n = int(input())

x = 0

oL = []
while x < n:
    i = input()
    if i == 'P=NP':
        oL.append('skipped')
    else:
        oL.append(eval(i))
    x+=1
    
print(*oL, sep ="\n")

