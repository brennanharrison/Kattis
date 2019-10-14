#!/usr/bin/env python
# coding: utf-8

# In[4]:


a,b,c = [int(x) for x in input().split()]

x = 0

if b-a < c-b:
    while b-a != c-b:
        b = b + 1
        a = b - 1
        x+=1
elif b-a > c-b:
    while b-a != c-b:
        b = b - 1
        c = b + 1
        x+=1
elif b-a == 1 and c-b == 1:
    x = 0
elif b-a == c-b:
     while b!= c-1:
        b = b + 1
        a = b - 1
        x+=1
print(x)

