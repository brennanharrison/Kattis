#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def closest(lst, K): 
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 



u = 0
c = int(input())
oTP = []
while (u<c):
    l,n = [int(x) for x in input().split()]
    a = []
    sTA = []
    oPL = []
    while len(a) < n:
        x = list(map(int,input().split()))
        for i in x:
            a.append(i)
  #print(len(a))
  #print(a)
    a.sort()
    for i in a:
        if i < l/2:
            h = i-0
            sTA.append(h)
        elif i >= 1/2:
            h = l-i
            sTA.append(h)
    oPL.append(max(sTA))
    
    j = closest(a,l)
    t = closest(a,0)
    
    if j-0 > l-t:
        #j = abs(j - l)
        oPL.append(j-0)
    else:
        #t = abs(t - l)
        oPL.append(l-t)
    
    u+=1
    #oPL.remove(oPL[1])
    oTP.append(oPL)
    
for i in oTP:
    a = i[0]
    b = i[1]
    print(str(a),str(b))

