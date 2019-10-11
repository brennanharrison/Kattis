#!/usr/bin/env python
# coding: utf-8

# In[17]:


def distinctCityNum(cityList, cityNum):
    t = 1
    p = []
    p.append(cityList[0])
    for i in cityList[1:]:
        if i in p:
            pass
        else:
            t+=1
            p.append(i)
    return t
            

        


n = int(input())

x = 0


outputList = []

while x < n:
    c = []
    nC = int(input())
    y = 0
    while y < nC:
        city = input()
        c.append(city)
        y+=1
    q = distinctCityNum(c, nC)
    outputList.append(q)
    x+=1
    
    
for i in outputList:
    print(i)
    


# In[ ]:




