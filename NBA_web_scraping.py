#!/usr/bin/env python
# coding: utf-8

# Method 1
# We could modularize the URL and year string of text that may be useful for programmatic access(in the subsequent code cell)

# In[1]:


# The building Blocks
year = '2019'
str = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

# Combining the URL + yer strings together
url = str.format(year)
url


# Now, lets programmatically return a list of URL gieven a list of years (e.g. 2015, 2016,2017,2018,2019)

# In[2]:


years = {2015, 2016,2017,2018,2019}
str = 'https://www.basketball-reference.com/leagues/NBA_{}_per_game.html'

# for loop
for year in years:
    url = str.format(year)
    print(url)


# Read HTML webpages into pandas

# In[6]:


url = 'https://www.basketball-reference.com/leagues/NBA_2019_per_game.html'


# In[4]:


import pandas as pd


# In[7]:


df = pd.read_html(url, header = 0)
df


# How many tables are there in the webpage?

# In[9]:


len(df)


# Select the first table

# In[10]:


df[0]


# In[11]:


# Since this webpage had only 1 table that's why we used df[0]
# Assigning the first table in df 2019 variable
df2019 = df[0]


# # Data Cleaning

# In[12]:


# We can see that the table header is presented multiple times in several rows.
# After every 20 rows in the tble, you can see there is a new header which we don't want in our analyses
# With this syntax, whenever we see 'Age' header, it will remove the whole header columns.
df2019[df2019.Age == 'Age']


# In[13]:


# So we removed all of the header columns in the table
# We have all the subsequent table selected in the entire data frame
# Now let's check the length
len(df2019[df2019.Age == 'Age']) # this checks the rows length which is 26 as you can see above


# In[14]:


# DROP function -
df = df2019.drop(df2019[df2019.Age == 'Age'].index)


# In[16]:


df.shape


# In[17]:


df2019.shape


# In[18]:


# AS you can see, before we had 734 rows with different header in our table
# AND now we just have 734 - 26 => 708 rows


# # Quick Exploratory Data Analysis

# In[19]:


import seaborn as sns


# Making the histogram

# In[ ]:


# We are going to use the histogram function called distplot
# PTS is the last variable name in our table
# kde= false Because we want to retain the original frequency
# if the kde=True, it will be the probability in shown (you can try)


# In[20]:


sns.distplot(df.PTS,kde=False)


# In[21]:


# Suppose we want to change the bar color, as you can see, it is transparent now

sns.distplot(df.PTS,
            kde=False,
            hist_kws= dict(edgecolor ="black", linewidth =2))


# Change the Bar fill Color

# In[22]:


sns.distplot(df.PTS,
            kde=False,
            hist_kws=dict(edgecolor = "black", linewidth =2)
            ,color='#00bFC4')


# In[ ]:




