#!/usr/bin/env python
# coding: utf-8

# In[1]:


p, n = [int(x) for x in input().split()]

l = []
t = []
x = 0
y = 0
z = 0

while x < n:
    u = input()
    l.append(u)
    x+=1
    
x = 0

while x < n:
    #print(z)
    if len(t) != p:
        if l[z] not in t:
            t.append(l[z])
    else:
        break
    x+=1
    z+=1
    #print(l)
    #print(t) 
    
    
if len(t) == p:
    print(z)
else:
    print('paradox avoided')


# In[ ]:





# In[ ]:




