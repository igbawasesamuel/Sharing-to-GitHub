#!/usr/bin/env python
# coding: utf-8

# # Working on fifa21 raw data v2.csv using jupyter notebook

# ## Data cleaning

# In[1]:


# importing the libraries and or packages that i will be needing for the cleaning process
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#reading the csv file
fifa_Data = pd.read_csv("fifa21 raw data v2.csv")


# In[3]:


fifa_Data


# In[10]:


# Looking out for null or missing values
fifa_Data.isnull()


# In[ ]:


# only Hits has null values among the columns.The total null values can be seeing below


# In[8]:


fifa_Data.isnull().sum()


# In[25]:


# Filling the missing values
fifa_Data.fillna(value = 0, inplace = True)


# In[26]:


fifa_Data.isnull().sum()
# notice that 'Hit' has 0 null or missing values now


# In[28]:


#checking for duplicate values
fifa_Data.duplicated().sum()


# In[29]:


# There are no duplicate values


# In[34]:


fifa_Data.columns


# In[35]:


fifa_Data.info()


# In[36]:


fifa_Data.iloc[:,11:20]


# In[37]:


fifa_Data.iloc[:,21:30]


# In[38]:


fifa_Data.iloc[:,31:40]


# In[39]:


fifa_Data.iloc[:,41:50]


# In[40]:


fifa_Data.iloc[:,51:60]


# In[41]:


fifa_Data.iloc[:,61:70]


# In[43]:


fifa_Data.iloc[:,71:77]


# In[50]:


# Correcting wrong datatype
fifa_Data['Joined'] = pd.to_datetime(fifa_Data['Joined'])

#notice that the dtype of 'Joined' which was initially object has change to datetime


# In[45]:


fifa_Data.info()


# In[48]:


# checking for incorrect datatype
fifa_Data.applymap(lambda x: isinstance(x,(int,float,str)))


# In[54]:


fifa_Data.head(21).iloc[:,1:21]


# In[ ]:




