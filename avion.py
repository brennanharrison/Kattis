#!/usr/bin/env python
# coding: utf-8

# In[13]:


x = 0

l = []
y = []

while x < 5:
    u = input()
    l.append(u)
    x+=1

h = 0   
for i in l:
    h+=1
    if 'FBI' in i:
        t = h
        y.append(str(t))
    
y.sort()

if y == []:
    print('HE GOT AWAY!')
else:
    print(' '.join(y))

