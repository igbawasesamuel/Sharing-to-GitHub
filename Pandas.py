#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


labels = ['a', 'b', 'c']
my_data = [20,30,40]
arr = np.array(my_data)
d ={'a':20, 'b':30, 'c':40}


# In[3]:


e = pd.Series(data=my_data)
e


# In[4]:


f = pd.Series(data=my_data, index=labels)
f


# In[5]:


type(f)


# In[6]:


g = pd.Series(d)
g


# ### Pandas DatarFame

# In[7]:


matrix_data=np.random.randint(1,20, size = 20).reshape(5,4)
matrix_data


# In[8]:


row_labels=['A','B','C','D','E']
column_label=['M','N','O','P']


# In[9]:


df=pd.DataFrame(matrix_data,index=row_labels, columns=column_label) 


# In[10]:


df


# ### reading CSV

# In[11]:


tip = pd.read_csv('tips.csv')
tip.head()


# In[12]:


tip.tail()


# In[13]:


tip.sample(20)


# In[14]:


tip.info()


# ### selecting column

# In[15]:


tip[["gender", "size"]]
# tip.gender


# ### filteringspecific rows and columns
# 

# In[16]:


tip[tip["gender"] == "Male"]


# In[17]:


tip[tip["size"] > 3]


# In[18]:


tip["day"].value_counts().sort_values(ascending=True)


# In[19]:


tip[(tip["day"] == "Sat") | (tip["day"] == "Sun")]


# In[20]:


tip[tip["day"].isin(["Sat", "Sun"])]


# In[21]:


tip[(tip["day"] == "Sat") & (tip["time"] == "Dinner")]


# In[22]:


tip.iloc[:500, 0:3]


# In[23]:


tip["total"] = tip["tip"] * tip["size"]


# In[24]:


tip


# In[25]:


tip.describe(include='all')


# In[63]:


tip.fillna(mean,inplace=True)


# In[38]:


tip_gender=tip.groupby('gender')
tip_gender


# In[26]:


tip.columns


# In[27]:


model = pd.read_excel('AI_Invasion_In-Class_Dataset.xlsx')


# In[28]:


model.head()


# In[41]:


labels =['Location','Maker','Model','Year','Colour','Amount', 'Type','Distance_Km']
car_df=pd.read_excel('AI_Invasion_In-Class_Dataset.xlsx',names=labels)
car_df


# In[29]:


model_subset= model.loc[:9,['Model','Year','Colour']]
model_subset


# In[61]:


maker.describe()


# In[39]:


maker= model.groupby('Maker')
maker.mean()


# In[62]:


maker.fillna(mean,inplace=True)


# In[59]:


car_df['Model'].unique()


# In[53]:


location_subset=car_df.groupby('Maker')
location_subset.sum()['Amount']


# In[31]:


model.info()


# In[32]:


model['Distance_Km'].isnull().sum()


# In[33]:


model['Year'].isnull().sum()


# In[34]:


model.describe()


# In[35]:


import matplotlib.pyplot as plt


# In[36]:


plt.plot(model['Distance_Km'], kind="line")


# In[ ]:


model.fillna(model['Distance_Km'].median())


# In[ ]:


plt.plot(model['Type'])


# In[ ]:





# In[ ]:


help(plt)


# In[ ]:


tip.loc[:,(tip>1).any()]


# In[ ]:





# In[ ]:





# In[ ]:




