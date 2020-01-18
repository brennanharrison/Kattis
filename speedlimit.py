#!/usr/bin/env python
# coding: utf-8

# In[3]:


i = []


while True:
    n = int(input())
    
    if n == -1:
        break
        
    x = 0
    q = 0
    l = 0
    j =[] 
    
    while x < n:
        if x == 0:
            x1,x2= [int(x) for x in input().split()]
            q = q + (x2*x1)
            j.append(x2)
        else:
            x1,x2= [int(x) for x in input().split()]
            q = q + ((x2-j[l])*x1)
            j.append(x2)
            l+=1
        x+=1
    
    i.append(q)
    
for u in i:
    print(u, 'miles')

