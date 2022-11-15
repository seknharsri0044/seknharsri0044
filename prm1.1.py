#!/usr/bin/env python
# coding: utf-8

# In[1]:


list = ['great','hello','hiyo','abc'] 

l=[]
for i in list:
    l.append(i)
ans=[]
ans=sorted(l,key=lambda s:s[-2])
print(ans)


# In[2]:


n=int(input('enter number'))
rev = 0
 
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
 
print(rev)


# In[ ]:




