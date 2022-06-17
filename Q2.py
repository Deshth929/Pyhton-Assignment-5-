#!/usr/bin/env python
# coding: utf-8

# In[9]:


number=int(input("Enter number: "))


# In[7]:


rang=int(input("Enter range: "))


# In[10]:


for i in range(rang):
    temp=number*i
    if (temp>rang):
        break
    print(temp)


# In[ ]:




