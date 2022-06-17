#!/usr/bin/env python
# coding: utf-8

# In[26]:


side1=int(input("Enter side1: "))


# In[27]:


side2=int(input("Enter side2: "))


# In[28]:


side3=int(input("Enter side3: "))


# In[29]:


if((side1+side2>side3)and(side2+side3>side1)and(side3+side1>side2)):
    s=((side1+side2+side3)/2)
    area=((s*(s-side1)*(s-side2)*(s-side3))**(1/2))
    
else:
    print("Triangle not possible")


# In[30]:


area


# In[ ]:




