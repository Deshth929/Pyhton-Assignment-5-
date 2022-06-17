#!/usr/bin/env python
# coding: utf-8

# In[59]:


number=int(input("Enter range: "))


# In[61]:


for i in range(1,number+1):
    k=0
    for j in range(2,i+1):
        if(i%j==0):
            break
        else:
            k+=1
    if(k==(i-2)):
        print(i)          


# In[ ]:




