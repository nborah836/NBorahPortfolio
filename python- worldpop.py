#!/usr/bin/env python
# coding: utf-8

# In[24]:


#import your relvant libriaies

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


#load data from its local or online storage **

df = pd.read_csv(r"C:\Users\Nbora\Downloads\world_population (1).csv")


# In[6]:


# "df" will give you a basic display of loaded data

df


# In[5]:


# should you wish to change format of data the following code can be used

pd.set_option('display.float_format', lambda x: '%.2f' % x)


# In[7]:


# basic info on data

df.info()


# In[8]:


# dr.describe to gain stat infor on data

df.describe()


# In[9]:


# check for null values in the data

df.isnull().sum()


# In[11]:


# see how many uniquie values are in the data. this may change depending on data set so use logic.
# IDs should have a uniquie value for every entry while 'departments' may not. keep that in mind.

df.nunique()


# In[12]:


#this will sort your command remeber that usually it will put smallest value at the top unless you tell it not to.

df.sort_values(by="World Population Percentage", ascending=False).head(10)


# In[13]:


# cammd will give you the correlations between values

df.corr()


# In[15]:


# a heat map of said correlations

sns.heatmap(df.corr(), annot = True)

plt.rcParams['figure.fisize'] = (20,7)

plt.show()


# In[16]:


# will group by continent then sort by 2022 population

df.groupby('Continent').mean().sort_values(by="2022 Population",ascending=False)


# In[17]:


# searching continent for data that contains "oceania" in the continent collum

df[df['Continent'].str.contains('Oceania')]


# In[18]:


# total populations by continent 

df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean().sort_values(by="2022 Population",ascending=False)
df2


# In[19]:


# your colums in data

df.columns


# In[20]:


#  transpose your data so populations are rows and cotinenr are colums

df3 = df2.transpose()
df3


# In[29]:


df3.plot(figsize=(20,10))


# In[28]:


df.boxplot(figsize=(20,10))


# In[23]:


df.select_dtypes(include='float')


# In[ ]:




