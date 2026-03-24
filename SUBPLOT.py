#!/usr/bin/env python
# coding: utf-8

# In[14]:


import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1,2,3,4]
plt.subplot(1,2,1)
plt.plot(x,y,color='r')
plt.pie([1],colors='g')
plt.subplot(1,2,1)
x2=[10,20,30,40]
plt.pie(x2)

x1=["x","y","c","d"]
y1=[1,2,3,4]
plt.bar(x1,y1)

plt.show()


# In[20]:


plt.subplot(1,2,1)
plt.subplot(1,2,2)
plt.show()


# In[23]:


plt.subplot(2,3,1)
plt.subplot(2,3,2)
plt.subplot(2,3,3)
plt.subplot(2,3,4)
plt.subplot(2,3,5)
plt.subplot(2,3,6)
plt.show()


# In[15]:


import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[1,2,3,4]
plt.subplot(2,2,1)
plt.plot(x,y,color='r')

plt.subplot(2,2,2)
plt.pie([1],colors='g')

plt.subplot(2,2,3)
x2=[10,20,30,40]
plt.pie(x2)



plt.subplot(2,2,4)
x1=["x","y","c","d"]
y1=[1,2,3,4]
plt.bar(x1,y1)

plt.show()


# In[ ]:




