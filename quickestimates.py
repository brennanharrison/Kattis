#!/usr/bin/env python
# coding: utf-8

# In[2]:


n = int(input())

x = 0

output = []

while x < n:
    i = input()
    output.append(len(i))
    x+=1
    
for i in output:
    print(i)

