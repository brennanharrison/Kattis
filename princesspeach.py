#!/usr/bin/env python
# coding: utf-8

# In[3]:


n,y = [int(x) for x in input().split()]

x = 0

d = []
while x < y:
    s = int(input())
    d.append(s)
    x+=1
    
d = set(d)
e = sorted(d)

output = []
for i in range(n):
    if i not in e:
        output.append(i)
        
for i in output:
    print(i)
print('Mario got ' + str(len(e)) + ' of the dangerous obstacles.')


# In[ ]:




