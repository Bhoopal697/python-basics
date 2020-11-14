#!/usr/bin/env python
# coding: utf-8

# In[2]:


# most watched netflix series or movies,recommendation,ratings


# In[4]:


import pandas as pd


# In[5]:


netflix=pd.read_csv('netflix_titles.csv')


# In[8]:


netflix.head(7)


# In[7]:


netflix.tail(6)


# In[11]:


netflix.describe()


# In[16]:


netflix.iloc[1:20,2:7]


# In[20]:


netflix.loc[1:20,'release_year']


# In[21]:


netflix['release_year']<2010


# In[22]:


netflix[netflix['release_year']<2010]


# In[23]:


# plot the graph


# In[26]:


from matplotlib import pyplot as plt


# In[27]:


plt.hist(netflix['release_year'])


# In[31]:


plt.hist(netflix['duration'])


# In[ ]:





# In[ ]:





# In[ ]:




