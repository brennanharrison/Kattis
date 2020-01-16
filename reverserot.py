#!/usr/bin/env python
# coding: utf-8

# In[32]:


st = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

ol = []
while True:
    p = 0
    x = [str(x) for x in input().split()]
    if x[0] == '0':
        break
    q = x[0]
    y = x[1]
    y = y[::-1]
    for i in y:
        e = st.index(i)
        e = e + int(q)
        if e > 27:
            e = e - 28
        i = st[e]
        y = list(y)
        y[p] = i
        y = ''.join(y)
        p+=1
    ol.append(y)
    
for i in ol:
    print(i)

