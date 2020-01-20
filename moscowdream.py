#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a, b, c, n = [int(x) for x in input().split()]

if a == 0 or b == 0 or c == 0:
    print('NO')
elif n == 1 or n == 2:
    print('NO')
elif a + b + c < n:
    print('NO')
else:
    print('YES')

