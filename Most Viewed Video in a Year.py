#!/usr/bin/env python
# coding: utf-8

# In[1]:


#libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


youtube_train_df = pd.read_csv('CAvideos.csv')


# In[3]:


youtube_train_df.head()


# In[4]:


youtube_train_df.isnull()


# In[5]:


sns.heatmap(youtube_train_df.isnull())


# In[6]:


youtube_train_df.drop('description' ,axis=1,inplace=True)


# In[7]:


youtube_train_df.drop('video_id' ,axis=1,inplace=True)


# In[8]:


youtube_train_df.drop('category_id' ,axis=1,inplace=True)


# In[ ]:


youtube_train_df.drop('thumbnail_link' ,axis=1,inplace=True)


# In[10]:


sns.heatmap(youtube_train_df.isnull())


# In[11]:


youtube_train_df.head()


# In[44]:


string = videos[0]
return int(string)


# In[41]:


youtube_train_df['views'] = np.asarray(youtube_train_df['views'], dtype=int)


# In[37]:


youtube_train_df = ["views", "publish_time"]
youtube_train_df1 = "views"
youtube_train_df2 = "publish_time"


# In[38]:


sns.distplot(youtube_train_df["views"])


# In[ ]:




