#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
x = 0
l = []
while x < n:
    q = input()
    l.append(q)
    x +=1

p = 0
for i in l:
    if 'CD' not in i:
        p+=1
    else:
        pass
    
print(p)

