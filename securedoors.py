#!/usr/bin/env python
# coding: utf-8

# In[19]:


n = int(input())

x = 0

iL = []
oL = []
memory = {}

while x < n:
    command = [str(x) for x in input().split()]
    iL.append(command)
    x+=1

for i in iL:
    if i[0] == 'entry' and (any(i[1] in s for s in oL) == False or memory[i[1]] == 'exit'):
        oL.append(i[1] +  ' entered')
        memory[i[1]] = 'enter'
    elif i[0] == 'entry' and memory[i[1]] == 'enter':
        oL.append(i[1] + ' entered ' + '(ANOMALY)')
    elif i[0] == 'exit' and (any(i[1] in s for s in oL) == False or memory[i[1]] == 'exit'):
        oL.append(i[1] + ' exited ' + '(ANOMALY)')
        memory[i[1]] = 'exit'
    elif i[0] == 'exit' and memory[i[1]] == 'enter':
        oL.append(i[1] + ' exited')
        memory[i[1]] = 'exit'
        
for i in oL:
    print(i)

