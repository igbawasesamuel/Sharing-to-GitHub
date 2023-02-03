#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12,4)


# In[ ]:


plt.plot(df1_.Drinks,df1_.Sales).xlabel('Drinks')
plt.ylabel('Sales')
plt.title('BAR STATISTICS')
plt.style.use('fivethirtyeight')
plt.show()


# In[ ]:


#using dictionary to create a DataFrame


# In[2]:


df1= {'Drinks':['B star','S star','B legend','S legend','Heineken','B maltina','pure heaven','Gulder','Life','Hero'],
     'Sales':[8,4,9,5,7,10,2,4,12,9],
     'Profit':[800,200,900,560,1200,480,400,300,520,450]}
df1_= pd.DataFrame(df1)
df1_


# In[ ]:


# making plots using matplotlib


# In[3]:


plt.plot(df1_.Drinks,df1_.Sales)
plt.xlabel('Drinks')
plt.ylabel('Sales')
plt.title('BAR STATISTICS')
plt.style.use('fivethirtyeight')
plt.show()


# In[4]:


plt.plot(df1_.Drinks,df1_.Profit)
plt.xlabel('Drinks')
plt.ylabel('Profit')
plt.title('BAR STATISTICS')
plt.text(6,5,'unusually low patronage')
plt.style.use('ggplot')
plt.show()


# In[29]:


plt.plot(df1_.Drinks,df1_.Profit, label ='Profit', color='green',linewidth=7)
plt.plot(df1_.Drinks,df1_.Sales, label='Sales',color='red',linewidth=5)
plt.xlabel('Drinks')
plt.ylabel('Profit')
plt.title('BAR STATISTICS')
plt.style.use('ggplot')
plt.title('plot title',fontsize =20)
plt.rcParams['figure.figsize']=(10,15) #used to increase the size ofb a plot(height,width)

plt.legend()


# In[6]:


family_data ={'members':['dad','mum','blessing','sam','janet','solo','joyce'],
             'age':[55,50,30,28,24,21,18],
             'height':[6,5.5,5,4.5,4,3.5,3],
             'position':[1,2,3,4,5,6,7]}
family_data1=pd.DataFrame(family_data)
family_data1


# In[7]:


plt.plot(family_data1.members,family_data1.age,label ='age', color='green',linewidth=7, linestyle='-', marker='d')
plt.plot(family_data1.members,family_data1.height,label ='height', color='orange',linewidth=5,linestyle='--', marker='x')
plt.plot(family_data1.members,family_data1.position,label ='position', color='blue',linewidth=3,linestyle=':', marker='x')
plt.xlabel('members')
plt.ylabel('age,height,position')
plt.title('Family Data')
plt.style.use('ggplot')
plt.title('plot title', fontsize=20)
plt.legend()


# In[8]:


df1_.info()


# In[9]:


plt.bar(df1_.Drinks,df1_.Sales)
plt.xlabel('Drinks')
plt.ylabel('Profit')
plt.title('BAR STATISTICS')
plt.text(5,5,'unusually low patronage')
plt.style.use('ggplot')


# In[10]:


plt.hist(df1_.Profit)
plt.xlabel('Profit')
plt.ylabel('Frequency')
plt.title('BAR STATISTICS')
#plt.text(6,5,'unusually low patronage')
plt.style.use('ggplot')


# In[30]:


plt.hist(family_data1.age)
plt.xlabel('age')
plt.ylabel(' family members')
plt.title('Family Data')
plt.style.use('ggplot')
plt.title('plot title', fontsize=20)
plt.legend()


# In[ ]:




