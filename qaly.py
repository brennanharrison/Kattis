#!/usr/bin/env python
# coding: utf-8

# In[6]:


def multiplyElements(argument):
    x = 1
    for i in argument:
        x*=i
    return x


n = int(input())

q = []

for i in range(n):
    i = []
    i = input().split()
    i = [float(x) for x in i]
    i = multiplyElements(i)
    q.append(i)


q = round(sum(q),3)




print(q)


# In[ ]:





# In[ ]:




