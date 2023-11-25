#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd
from numpy.random import randn
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings("ignore")

from sklearn.impute import SimpleImputer

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# In[29]:


data = pd.read_csv('C:/Users/7zl2oom/Desktop/california/housing.csv')
data
                   


# In[30]:


data.head()


# In[31]:


data.info()


# In[32]:


data.isnull().sum()


# In[33]:


data["ocean_proximity"].value_counts()


# In[34]:


data["ocean_proximity"].hist()


# In[35]:


data.describe()


# In[36]:


data.describe(include=[object])


# In[37]:


data.columns


# In[12]:


col=['longitude', 'latitude', 'housing_median_age',
     'total_rooms', 'total_bedrooms', 'population',
     'households', 'median_income','median_house_value']
fig, axes= plt.subplots(ncols=3,nrows=3,figsize=(30,20))
for i, column in enumerate(col):
    sns.distplot(data[column],ax=axes[i//3,i%3])
plt.show()    
    


# In[38]:


from sklearn.model_selection import train_test_split
train_set,test_set=train_test_split(data,test_size=0.2,random_state=1234)
train_set['median_income'].value_counts()/len(train_set)


# In[39]:


test_set['median_income'].value_counts()/len(test_set)


# In[40]:


data['income_bin']=pd.cut(data['median_income'], bins=[0.0,1.5,3.0,4.5,6.0,np.inf],labels=[1,2,3,4,5])
data['income_bin'].hist()


# In[41]:


from sklearn.model_selection import StratifiedShuffleSplit
split=StratifiedShuffleSplit(n_splits=1, random_state=1234)
for train_index, test_index in split.split(data,data['income_bin']):
    startfied_train= data.loc[train_index]
    startfied_test= data.loc[test_index]
    


# In[42]:


startfied_train['income_bin'].value_counts()/len(startfied_train)


# In[43]:


startfied_test['income_bin'].value_counts()/len(startfied_test)


# In[44]:


data


# In[45]:


data_copy=data.copy()
data_copy.drop('ocean_proximity',axis=1,inplace=True)
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imp_mean.fit(data_copy)
data = imp_mean.transform(data_copy)


# In[46]:


data = pd.DataFrame(data,columns=data_copy.columns,index=data_copy.index)
data.isnull().sum()


# In[47]:


from sklearn.preprocessing import OrdinalEncoder
enc = OrdinalEncoder()
X = enc.fit_transform(data)
X[:10]


# In[48]:


data.info()


# In[49]:


data


# In[50]:


data.count()


# In[51]:


data['population'].min()


# In[ ]:


sns.displot(data['total_rooms'])


# In[ ]:


plt.figure(figsize=(15,10))
sns.heatmap(data.corr(), annot=True, cmap='pink')


# In[ ]:


data.hist(figsize=(15,10))


# In[ ]:


from sklearn.model_selection import train_test_split

X = data.drop(['median_house_value'], axis=1)
y = data['median_house_value']

display(X)
display(y)


# In[ ]:


sns.jointplot(x='households',y='total_rooms',data=data,kind='scatter')


# In[ ]:


sns.jointplot(x='households',y='total_rooms',data=data,kind='reg')


# In[ ]:


sns.jointplot(x='total_bedrooms',y='housing_median_age',data=data,kind='hex')


# In[ ]:


sns.pairplot(data)


# In[ ]:


sns.pairplot(data,hue='median_income',palette='coolwarm')


# In[ ]:


sns.heatmap(data.corr())


# In[ ]:


sns.heatmap(data.corr(),cmap='coolwarm',annot=True)


# In[ ]:


ds = data.pivot_table(values='median_income',index='total_bedrooms',columns='households')
sns.heatmap(ds)


# In[ ]:


cor = data.corr()
cor['median_house_value'].sort_values(ascending=False)


# In[ ]:


data['ocean_proximity'].value_counts()


# In[ ]:


fig = plt.figure(figsize=(5,5))
data['ocean_proximity'].value_counts().plot(kind = 'pie', autopct='%.1f%%')
plt.ylabel(" ", fontsize = 15)
plt.title("ocean_proximity")
print("")


# In[ ]:


sns.scatterplot(x='median_house_value',y="housing_median_age",data=data,alpha=0.2)


# In[ ]:



sns.boxplot(y="total_rooms",data=data,color="r");


# In[ ]:


plt.figure(figsize=(18,18))
sc = plt.scatter(data["longitude"],
                 data["latitude"],
                 alpha=0.4,
                 cmap="mako",
                 c=data["median_house_value"],
                s=data["population"]/50,
                label='population')
plt.colorbar(sc)
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.title("longitude vs latitude")
plt.legend()
plt.show()


# In[ ]:


sns.distplot(data['median_house_value'])
plt.show()


# In[1]:


X = data.iloc[:, 1:2].values 
Y = data.iloc[:, -1].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)


# In[48]:


plt.scatter(X,Y, color='red' , label='train')


# In[ ]:


plt.scatter(X,Y, color='red' , label='train')
plt.plot(X,model.fit(X_train, Y_train).predict(X),color='black',label='line')


# In[ ]:




