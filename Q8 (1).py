#!/usr/bin/env python
# coding: utf-8

# In[1]:


list=[]
for i in range(1,11):
    str="Enter your {}th number: "
    number=int(input(str.format(i)))
    list.append(number)


# In[2]:


list


# In[3]:


print("Positive numbers: ",end="")
set1={0}
for i in range(1,10):
    if(list[i]>0):
        set1.add(list[i])
set1.remove(0)
print(set1)


# In[4]:


print("Negative numbers: ",end="")
set1={0}
for i in range(1,10):
    if(list[i]<0):
        set1.add(list[i])
set1.remove(0)
print(set1)


# In[5]:


print("Odd numbers: ",end="")
set1={0}
for i in range(1,10):
    if(list[i]%2!=0):
        set1.add(list[i])
set1.remove(0)
print(set1)


# In[6]:


print("Even numbers: ",end="")
set1={0}
for i in range(1,10):
    if(list[i]%2==0):
        set1.add(list[i])
set1.remove(0)
print(set1)


# In[7]:


for i in range(10):
    k=0
    temp = 0
    for z in range(i):
        if ((list[z] == list[i]) and (z != i)):
            temp += 1
    if(temp==0):
        for j in range(10):
            if (list[i]==list[j]):
                k+=1
        final="The number {} occurs {} time(s)"
        print(final.format(list[i],k))


# In[ ]:




