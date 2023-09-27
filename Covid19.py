#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotly.subplots import make_subplots
from datetime import datetime


# In[3]:


covid_df=pd.read_csv("covid_19_india.csv")


# In[4]:


covid_df.head()


# In[5]:


covid_df.info()


# In[6]:


covid_df.describe()


# In[7]:


vaccine_df=pd.read_csv("covid_vaccine_statewise.csv")


# In[8]:


vaccine_df.head(10)


# In[9]:


covid_df.drop(["Sno", "Time", "ConfirmedIndianNational", "ConfirmedForeignNational"], inplace = True, axis = 1)


# In[10]:


covid_df.head()


# In[11]:


covid_df['Date'] = pd.to_datetime(covid_df['Date'], format = '%Y-%m-%d')


# In[12]:


covid_df.head()


# In[13]:


# active cases

covid_df['Active_Cases'] = covid_df['Confirmed'] - (covid_df['Cured'] + covid_df['Deaths'])


# In[14]:


covid_df.tail(100)


# In[15]:


statewise = pd.pivot_table(covid_df, values = ["Confirmed", "Deaths", "Cured"], index = "State/UnionTerritory", aggfunc = max)


# In[18]:


statewise["Recovery Rate"] = statewise["Cured"]*100/statewise['Confirmed']


# In[19]:


statewise["Mortality Rate"] = statewise["Deaths"]*100/statewise['Confirmed']


# In[22]:


statewise = statewise.sort_values(by = "Confirmed", ascending = False)


# In[23]:


statewise.style.background_gradient(cmap = "cubehelix")


# In[37]:


# top 10 states with the most active cases
top_10_active_cases = covAid_df.groupby(by = 'State/UnionTerritory').max()[['Active_Cases', 'Date']].sort_values(by = ['Active_Cases'], ascending = False).reset_index()


# In[39]:


fig=plt.figure(figsize=(16,9))


# In[41]:


plt.title('Top 10 states with most active cases in India', size = 25)


# In[45]:


ax = sns.barplot(data = top_10_active_cases.iloc[:10], y = 'Active_Cases', x = 'State/UnionTerritory', linewidth = 2, edgecolor = 'red')


# In[50]:


# top 10 states with the most active cases
top_10_active_cases = covid_df.groupby(by = 'State/UnionTerritory').max()[['Active_Cases', 'Date']].sort_values(by = ['Active_Cases'], ascending = False).reset_index()
fig=plt.figure(figsize=(16,9))
plt.title('Top 10 states with most active cases in India', size = 25)
ax = sns.barplot(data = top_10_active_cases.iloc[:10], y = 'Active_Cases', x = 'State/UnionTerritory', linewidth = 2, edgecolor = 'red')
plt.xlabel("States")
plt.ylabel("Total Activee Cases")
plt.show()


# In[59]:


# top 10 states with most deaths

top_10_deaths = covid_df.groupby(by = 'State/UnionTerritory').max()[['Deaths', 'Date']].sort_values(by = ['Deaths'], ascending = False).reset_index()

fig = plt.figure(figsize = (18,5))

plt.title("top 10 states with most deaths", size = 25)

ax = sns.barplot(data = top_10_deaths.iloc[:12], y = 'Deaths', x = 'State/UnionTerritory', linewidth = 2, edgecolor = 'black')

plt.xlabel("states")
plt.ylabel("Deaths")
plt.show()


# In[79]:


# growth trend

fig = plt.figure(figsize= (12,6))
 
ax = sns.lineplot( data = covid_df[covid_df['State/UnionTerritory'].isin(['Maharashtra', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Uttar Pradesh'])], x = 'Date', y = 'Active_Cases', hue = 'State/UnionTerritory')
                                   
ax.set_title("Top 5 affected states in INDIA", size = 20)


# In[80]:


# starting for the vaccine dataset now
vaccine_df.head()


# In[81]:


vaccine_df.rename(columns = {'Updated On': 'Vaccine_date'}, inplace = True)


# In[82]:


vaccine_df.head(10)


# In[83]:


vaccine_df.info()


# In[85]:


vaccine_df.isnull().sum()


# In[86]:


vaccination = vaccine_df.drop(columns  = ['Sputnik V (Doses Administered)', 'AEFI', '18-44 Years (Doses Administered)', '45-60 Years (Doses Administered)', '60+ Years (Doses Administered)'], axis = 1)


# In[88]:


vaccination.head()


# In[91]:


# male vs female vaccination

male = vaccination['Male(Individuals Vaccinated)'].sum()
female = vaccination['Female(Individuals Vaccinated)'].sum()
px.pie(names = ["Male", "Female"], values=[male, female], title = "male and female vaccination")


# In[96]:


# remove rows where stae is  = India

vaccine = vaccine_df[vaccine_df.State!='India']
vaccine
vaccine.rename(columns = {'Total Individuals Vaccinated' : 'Total'}, inplace = True)
vaccine.head()


# In[98]:


# most vaccinated state
   
max_vac = vaccine.groupby('State')['Total'].sum().to_frame('Total')
max_vac = max_vac.sort_values('Total',ascending = False)[:5]
max_vac


# In[99]:


fig = plt.figure(figsize=(10,5))
plt.title("Top 5 Vaccinated States in India", size  = 20)
x = sns.barplot(data = max_vac.iloc[:10], y = max_vac.Total, x = max_vac.index, linewidth = 2, edgecolor='black')
plt.xlabel("States")
plt.ylabel("Vaccination")
plt.show


# In[ ]:




