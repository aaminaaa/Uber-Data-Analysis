#!/usr/bin/env python
# coding: utf-8

# In[72]:


# Plotting Functions
get_ipython().run_line_magic('pylab', 'inline')

# Data Manipulation 
import pandas

# Visualization
import seaborn


# In[73]:


# Import data (.csv)
data = pandas.read_csv('Desktop/Data Visualization/uber-raw-data-apr14.txt')


# In[74]:


data 


# In[75]:


data.tail()


# In[76]:


# Convert datetime to usable form and add columns


# In[77]:


data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)


# In[78]:


data.tail()


# In[79]:


# Function to create a column containing the date of the month
def retrieve_dom(dt):
    return dt.day

data['dom'] = data['Date/Time'].map(retrieve_dom)


# In[80]:


data.tail()


# In[81]:


# Function to create a column containing the day of the week
def retrieve_weekday(dt):
    return dt.weekday()

data['weekday'] = data['Date/Time'].map(retrieve_weekday)

def retrieve_hour(dt): 
    return dt.hour

data['hour'] = data['Date/Time'].map(retrieve_hour)

data.tail()


# In[ ]:


# Analysis


# In[ ]:


## analyze data form


# In[113]:


hist(data.dom, bins = 30, rwidth = 0.8, range = (0.5, 30.5))
# axis labels and head title
xlabel('Date of the Month')
ylabel('Frequency')
title('Frequency by DoM - uber - Apr 2014')


# In[92]:


# Provides the number of records for each day of the month
def count_rows(rows):
    return len(rows)
by_date = data.groupby('dom').apply(count_rows)
by_date


# In[145]:


# Sorts the data set by the number of records for
# each day of the month (smallest to largest) 
bar(range(1, 31), by_date_sorted)
xticks(range(1,31), by_date_sorted.index)
# Axis labels and head title
xlabel('Date of the Month')
ylabel('Frequency')
title('Frequency by Days of the Month - Uber - Apr 2014')
# Hides unnecessary outputs
("")


# In[ ]:


# Analyze the hour


# In[121]:


hist(data.hour, bins = 24, range = (0.5, 24))


# In[173]:


hist(data.weekday, bins = 7, range = (-0.5, 6.5), rwidth = 0.8, color = '#FB6A68', alpha = 0.8)
xticks(range(7), 'Mon Tue Wed Thu Fri Sat Sun'.split())
# Axis labels and head title
xlabel('Days of the Week')
ylabel('Frequency')
title('Frequency by Days of the Week - Uber - Apr 2014')
# Hides unnecessary outputs
("")


# In[174]:


# Cross analysis (hour, dow)


# In[175]:


by_cross = data.groupby('weekday hour'.split()).apply(count_rows).unstack()


# In[179]:


seaborn.heatmap(by_cross)


# In[ ]:


# By latitude and longitude


# In[188]:


hist(data['Lat'], bins = 100, range = [40.5, 41])
# Hides unnecessary outputs
("")


# In[191]:


hist(data['Lon'], bins = 100, range = [-74.5, -73.9])
# Hides unnecessary outputs
("")


# In[205]:


hist(data['Lon'], bins = 100, range = [-74.1, -73.9], color = 'r', alpha = 0.5, label = 'Longitude')
legend(loc = 'upper left')
twiny()
hist(data['Lat'], bins = 100, range = [40.5, 41], color = 'b', alpha = 0.5, label = 'Latitude')
legend(loc = 'best')
# Hides unnecessary outputs
("")


# In[211]:


plot(data['Lat'], '.', ms = 3, color = 'green', label = 'Latitude')
xlim(0, 100)
grid()


# In[220]:


figure(figsize = [20, 20])
plot(data['Lon'], data['Lat'], '.', ms = 1, alpha = 0.5)
xlim(-74.2, -73.7)
ylim(40.7, 41)


# In[ ]:





# In[ ]:




