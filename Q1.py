#!/usr/bin/env python
# coding: utf-8

# In[1]:


string=input("Enter the string: ")


# In[3]:


name=""
for i in string:
    name=i+name
print(name)

