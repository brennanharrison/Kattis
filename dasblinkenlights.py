#!/usr/bin/env python
# coding: utf-8

# In[37]:


p,q,s= [int(x) for x in input().split()] # Get the data

   
k = list(range(0,s+1,p)) # Build a range of multiples for p until the last element <= s.
y = list(range(0,s+1,q)) # Build a range of multiples for q until the last element <= s.


k = k[1:] # Remove first element from first range.
y = y[1:] # Remove first element from second range.

u = [i for i in k + y if i in k and i in y] # Concatenate first range to second range and only return elements that exist in both lists.
u = set(u) # Return only unique elements.

j = [i for i in u if i <= s] # Return elements <= s.

# If multiples exist in both initial ranges that are <= s, print.
if len(j) > 0:
    print('yes')
else:
    print('no')

