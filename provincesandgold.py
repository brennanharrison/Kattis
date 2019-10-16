#!/usr/bin/env python
# coding: utf-8

# In[4]:


goldPower = 3
silverPower = 2
copperPower = 1

g, s, c = [int(x) for x in input().split()]

g = g*goldPower
s = s*silverPower
c = c*copperPower

t = g + s + c

if t >= 8:
    print('Province or Gold')
elif t >= 6:
    print('Duchy or Gold')
elif t >= 5:
    print('Duchy or Silver')
elif t >= 3:
    print('Estate or Silver')
elif t >= 2:
    print('Estate or Copper')
else:
    print('Copper')

