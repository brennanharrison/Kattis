#!/usr/bin/env python
# coding: utf-8

# In[131]:


n = int(input())
i = 0

if 1 <= n <= 10000000:
    while True:
        i = i + 2
        n = n - i
        if i >= n and n%2==1:
            print("Alice") 
            break
        elif i >= n and n%2==0:
            print("Bob")
            break


# ## 

# ## 2

# In[ ]:




