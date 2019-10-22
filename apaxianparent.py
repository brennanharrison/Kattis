#!/usr/bin/env python
# coding: utf-8

# In[6]:


vowels = ['a', 'i', 'o', 'u']

first, last = [str(x) for x in input().split()]

if first[-1] == 'e':
    print(first+'x'+last)
elif first[-1] in vowels:
    first = first[:-1]
    print(first+'ex'+last)
elif first[-2:] == 'ex':
    print(first+last)
else:
    print(first+'ex'+last)

