#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Programmer: Brennan Harrison
# Date: 09/06/2019
# Problem ID: dicecup


userList = [int(x) for x in input().split()]
n = userList[0]
m = userList[1]

q = n + 1
u = m + 1

if n == m:
    print(n + 1)
elif n > m:
    while(u <= q):
        print(u)
        u = u + 1
else:
    while(q <= u):
        print(q)
        q = q + 1


# In[ ]:





# ##### 
