#!/usr/bin/env python
# coding: utf-8

# In[1]:


import decimal
c = int(input())
def average(gradeList, studentNum):
    gradeAverage = round(decimal.Decimal(sum(gradeList)) / decimal.Decimal(studentNum),3)
    aboveAverage = 0
    for i in gradeList:
        if i > gradeAverage:
            aboveAverage +=1
    aboveAverage = round(((decimal.Decimal(aboveAverage)/ decimal.Decimal(studentNum))* (100)),3)
    return aboveAverage
percentAboveAverage = []
x = 1
while (x <= c):
    u = input().split()
    u = [int(x) for x in u]
    r = u[0]
    u.remove(u[0])
    y = average(u,r)
    percentAboveAverage.append(y)
    x+=1
for i in percentAboveAverage:
    print(str(i) + "%")

