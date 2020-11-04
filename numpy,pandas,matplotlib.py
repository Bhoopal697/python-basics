#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#single dimensional numpy array


# In[5]:


n1=np.array([10,20,30,40,50])
n1


# In[6]:


type(n1)


# In[7]:


#multi dimensional numpy array


# In[9]:


n2 = np.array([[10,20,30],[30,20,10]])
n2


# In[10]:


type(n2)


# In[11]:


#initilizing numpy array with zeroes


# In[12]:


n1 = np.zeros((1,2))
n1


# In[13]:


n1 = np.zeros((6,6))
n1


# In[14]:


#initializing numpy array with the same number


# In[15]:


n1 = np.full((2,2),10)
n1


# In[16]:


n1 = np.full((4,4),2)
n1


# In[17]:


#initializing numpy array within a range


# In[18]:


n1 = np.arange(1,11)
n1


# In[19]:


n1 = np.arange(10,100,10)
n1


# In[23]:


n1 = np.random.randint(100,200,10)
n1


# In[24]:


# checking the shape of numpy array


# In[26]:


n1 = np.array([[1,2,3,4],[5,6,7,8]])
n1


# In[30]:


n1.shape


# In[31]:


n1.shape=(4,2)


# In[32]:


n1


# In[33]:


#addition of numpy arrays


# In[34]:


n1 = np.array([10,20])
n2 = np.array([30,40])


# In[35]:


np.sum([n1,n2])


# In[38]:


np.sum(([n1,n2]),axis=0)


# In[39]:


np.sum(([n1,n2]),axis=1)


# In[40]:


#joining numpy arrays


# In[41]:


n1 = np.array([10,20,30])
n2 = np.array([40,50,60])


# In[42]:


np.vstack((n1,n2))


# In[43]:


np.hstack((n1,n2))


# In[44]:


np.column_stack((n1,n2))


# In[1]:


# pandas


# In[2]:


import pandas as pd


# In[9]:


s1=pd.Series([1,2,3,4,5])
s1


# In[10]:


type(s1)


# In[11]:


#changing index


# In[12]:


s1 = pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
s1


# In[13]:


# series of objects from the list


# In[17]:


s1=pd.Series({'a':10,'b':20,'c':30})
s1


# In[18]:


# another method


# In[20]:


d1 = {'a':25,'b':69,'c':88,'d':99}


# In[21]:


pd.Series(d1)


# In[22]:


# pandas data frame


# In[25]:


student = {"student_names":['anup','harish','bhoopal','sam','shalom','enoch','deva'],"student_marks":[87,13,99,64,96,45,78]}


# In[26]:


pd.DataFrame(student)


# In[27]:


# importing files


# In[28]:


import pandas as pd


# In[33]:


googleplaystore= pd.read_csv('googleplaystore.csv')


# In[35]:


googleplaystore.head()


# In[38]:


googleplaystore.tail()


# In[39]:


googleplaystore.head(10)


# In[41]:


googleplaystore.tail(15)


# In[42]:


googleplaystore.describe()


# In[46]:


googleplaystore1=googleplaystore.iloc[25:50,2:4]


# In[50]:


googleplaystore


# In[56]:


googleplaystore2 = googleplaystore.iloc[10:21,[0,5]]


# In[57]:


googleplaystore2


# In[58]:


googleplaystore3 = googleplaystore.loc[10:30,("App","Installs","Size","Type","Price")]


# In[ ]:





# In[59]:


googleplaystore3


# In[60]:


googleplaystore['Rating']>4.5


# In[61]:


googleplaystore[googleplaystore['Rating']>4.5]


# In[63]:


# MATPLOTLIB (used for data visualization)


# In[64]:


from matplotlib import pyplot as plt


# In[65]:


import numpy as np


# In[67]:


x = np.arange(1,11)


# In[68]:


x


# In[69]:


y = 2*x
y


# In[81]:


plt.plot(x,y,linewidth='2',linestyle=':',color='red')
plt.grid()
plt.title("x vs y axis")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()


# In[82]:


# ploting for 2 lines


# In[83]:


from matplotlib import pyplot as plt


# In[84]:


import numpy as np


# In[92]:


x = np.arange(1,11)


# In[93]:


x


# In[94]:


y1 = 2*x
y2 = 3*x


# In[95]:


y1,y2


# In[103]:


plt.plot(x,y1)
plt.plot(x,y2)
plt.grid()
plt.title(" line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()


# In[104]:


# Bar Plot


# In[105]:


student={"Sam":65,"bhoopal":50,"ram":99}


# In[106]:


names = list(student.keys())
marks = list(student.values())


# In[107]:


names,marks


# In[114]:


plt.barh(names,marks,color='green')
plt.title(" bar graph")
plt.xlabel(" name of the student")
plt.ylabel("marks of students")
plt.show()


# In[115]:


# if you add h in plt.bar , the graph shows in horizontal 


# In[116]:


# scatter-plot


# In[117]:


x = [5,6,8,9,5,5]
y = [6,7,8,5,6,2]


# In[119]:


plt.scatter(x,y)
plt.grid()
plt.show()


# In[ ]:




