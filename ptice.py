#!/usr/bin/env python
# coding: utf-8

# In[5]:


a = 'ABC'
b = 'BABC'
g = 'CCAABB'

x = 0
y = 0
z = 0
ar = 0
br = 0
gr = 0
ol = []

n = int(input())

q = input()

for i in q:
    if i == a[x]:
        ar+=1
    if i == b[y]:
        br+=1
    if i == g[z]:
        gr+=1
    
    if x == len(a)-1:
        x = 0
    else:
        x+=1
    if y == len(b)-1:
        y = 0
    else:
        y+=1
    if z == len(g)-1:
        z = 0
    else:
        z+=1
    
if ar == br and ar == gr:
    ol.append(ar)
    ol.append('Adrian')
    ol.append('Bruno')
    ol.append('Goran')
elif ar > br and ar > gr:
    ol.append(ar)
    ol.append('Adrian')
elif br > ar and br > gr:
    ol.append(br)
    ol.append('Bruno')
elif gr > ar and gr > br:
    ol.append(gr)
    ol.append('Goran')
elif ar == br and ar > gr:
    ol.append(ar)
    ol.append('Adrian')
    ol.append('Bruno')
elif ar == gr and ar > br:
    ol.append(ar)
    ol.append('Adrian')
    ol.append('Goran')
elif br == gr and br > ar:
    ol.append(br)
    ol.append('Bruno')
    ol.append('Goran')
    
for i in ol:
    print(i)

