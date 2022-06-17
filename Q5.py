#!/usr/bin/env python
# coding: utf-8

# In[53]:


rows=int(input("Enter number of rows: "))


# In[54]:


k=0
for i in range(rows):
    for j in range(i+1):
        print(chr(k+65),end="")
        if(chr(k+65)=='Z'):
            k=-1
        k+=1
            
    print("")


# In[ ]:




