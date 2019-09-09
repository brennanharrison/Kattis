#!/usr/bin/env python
# coding: utf-8

# In[1]:


text = input()

uppers = []
lowers = []

for word in text.split("-"):
    if word[0].isupper():
        uppers.append(word)
    else: 
        lowers.append(word)

upperCaseLetter = []
lowerCaseLetter = []

for letter in uppers:
    if letter[0].isupper():
        upperCaseLetter.append(letter[0])
    else:
        lowers.append(letter)

        
newList = ''.join(upperCaseLetter)
print(newList)


# In[ ]:




