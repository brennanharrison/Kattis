#!/usr/bin/env python
# coding: utf-8

# In[6]:


import collections
n = int(input())

x = 0 
y = 1
output = []

while x<n:
    g = int(input())
    l = [int(x) for x in input().split()]
    i = list([item for item, count in collections.Counter(l).items() if count == 1])
    output.append('Case #' + str(y) +': ' + str(i[0]))
    x+=1
    y+=1
    
for i in output:
    print(i)

