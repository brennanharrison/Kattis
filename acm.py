#!/usr/bin/env python
# coding: utf-8

# In[7]:


lt = {}
lr = {}
x = 0
y = 0

while True:
    e = list(input().split())
    if e[0] == '-1':
        break
        
    t = int(e[0])
    p = e[1]
    r = e[2]
    
    if p not in lt.keys() and p not in lr.keys():
        if r == 'right':
            lt[p] = x + t
            lr[p] = r
        else:
            x = 20
            lt[p] = x
            lr[p] = r
    elif p in lt.keys() and p in lr.keys() and r == 'wrong' and lr[p] == r:
        x = 20
        lt[p] = lt[p] + x
    elif p in lt.keys() and p in lr.keys() and r == 'right' and lr[p] == r:
        pass
    elif p in lt.keys() and p in lr.keys() and r == 'right' and lr[p] != r:
        x = 0
        lt[p] = lt[p] + t
        lr[p] = r
    x = 0
    
i = []    
for key in lr:
    if lr[key] == 'right':
        y+=1
        i.append(key)
    
    
f = 0
for key in lt:
    if key in i:
        f+=lt[key]
        
        
print(y, f)


# In[ ]:




