#!/usr/bin/env python
# coding: utf-8

# In[2]:


def missingLetters(string):
    missing = ''
    for i in alphabet:
        if i not in string:
            missing = missing + i
    #print(missing)
    if missing != '':
        output.append('missing ' + missing)
    else:
        output.append('pangram')


n = int(input())

x = 0

missing = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
output = []


while x < n:
    s = input()
    m = s.replace(' ', '')
    p = m.translate({ord(i): None for i in ' '})
    t = p.translate({ord(i): None for i in '.,?!"'})
    e = t.translate({ord(i): None for i in "'"})
    r = e.translate({ord(i): None for i in '0123456789'})
    j = r.lower()
    missingLetters(j)
    x+=1
    
for i in output:
    print(i)

