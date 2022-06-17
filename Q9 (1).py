#!/usr/bin/env python
# coding: utf-8

# In[36]:


number=int(input("Enter number of words: "))
list=[]
for i in range(number):
    entry=input("Enter your word: ")
    list.append(entry)


# In[37]:


for i in range(number):
    k=1
    temp=0
    for z in range(i):
        if((list[z]==list[i])and(z!=i)):
            temp+=1
    if(temp==0):
        for j in range(number):
            if(list[i]==list[j] and i!=j):
                k+=1
        str="{} occurs {} time(s)"
        print(str.format(list[i],k))


# In[ ]:




