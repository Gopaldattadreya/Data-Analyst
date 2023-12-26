#!/usr/bin/env python
# coding: utf-8

# In[81]:


pwd


# # importing the libaries

# In[82]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# In[83]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


# # loading the data set

# In[84]:


df =pd.read_csv('hotel_bookings 2.csv')


# # EDA (Expolatrory Data Analysis)

# In[85]:


df.head(2)


# In[86]:


df.shape


# In[87]:


df.dtypes


# In[88]:


df.info()


# In[89]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'],dayfirst=True)


# In[90]:


df.info()


# In[91]:


df.describe(include='object')


# In[92]:


df.hotel.unique()


# In[93]:


for col in df.describe(include='object').columns:
    print(col)
    print('xxxxxxxxx'*8)
    print(df[col].unique())


# In[94]:


df.isnull().sum().sort_values(ascending=False)


# In[95]:


df.drop(['company','agent'],inplace=True,axis=1)


# In[96]:


df.dropna(inplace=True)


# In[97]:


df.describe()


# In[98]:


plt.boxplot(x=df['adr'])


# In[99]:


df=df[df['adr']<5000]


# In[100]:


df.describe()


# # Data Analysis & Visulizations

# In[146]:


df.is_canceled.value_counts(normalize=True)

plt.figure(figsize=(7,6))
plt.title('hotel booking reservation status')
plt.bar(['not canceled','canceled'],df.is_canceled.value_counts(),width=0.8,)
plt.savefig('ana1.png')
plt.show()


# In[147]:


plt.figure(figsize=(12,6))
sns.countplot(x='hotel',hue='is_canceled',data=df)
plt.title('reservation status in city & resort hotel')
plt.xlabel('hotel type')
plt.ylabel('no of reservations')
plt.savefig('ana2.png')
plt.show()


# In[103]:


resort_hotel=df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[104]:


City_hotel=df[df['hotel']=='City Hotel']
City_hotel['is_canceled'].value_counts(normalize=True)


# df.head(2)

# In[105]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
City_hotel = City_hotel.groupby('reservation_status_date')[['adr']].mean()
resort_hotel.head()


# In[149]:


plt.figure(figsize=(16,8))
plt.plot(resort_hotel.index,resort_hotel['adr'],label='resort_hotel')
plt.plot(City_hotel.index,City_hotel['adr'],label='city_hotel')
plt.title('ADR in city Vs resort hotel ',fontsize=20)
plt.legend()
plt.savefig('ana3.png')
plt.show()


# In[107]:


df.shape


# In[153]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(17,9))
sns.countplot(x='month',hue='is_canceled',data=df)
plt.title('Reservation status per month',fontsize=20)
plt.ylabel('no of reservations')
plt.legend(fontsize=20)
plt.savefig('ana6.png')
plt.show()



# In[152]:


dff=df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index()

plt.figure(figsize=(16,8))
plt.title('ADR per month',fontsize=20)
sns.barplot(x='month',y='adr',data=dff)
plt.savefig('ana5.png')

plt.show()


# In[154]:


canceled_data = df[df['is_canceled']==1]
top_10_countries = canceled_data['country'].value_counts()[:10]
plt.figure(figsize=(10,8))
plt.pie(top_10_countries,autopct='%.2f',labels=top_10_countries.index)
plt.title('top 10 countries that shows cancellation')
plt.savefig('ana7.png')
plt.show()


# In[111]:


df['market_segment'].value_counts()


# In[112]:


df['market_segment'].value_counts(normalize=True)


# In[113]:


canceled_data['market_segment'].value_counts(normalize=True)


# In[132]:


canceled_df_adr=canceled_data.groupby('reservation_status_date')[['adr']].mean()
canceled_df_adr.reset_index(inplace=True)
canceled_df_adr.sort_values('reservation_status_date',inplace=True)
not_canceled_data=df[df['is_canceled']==0]




not_canceled_df_adr=not_canceled_data.groupby('reservation_status_date')[['adr']].mean()
not_canceled_df_adr.reset_index(inplace=True)
not_canceled_df_adr.sort_values('reservation_status_date',inplace=True)

plt.figure(figsize=(20,8))

plt.plot(not_canceled_df_adr['reservation_status_date'],not_canceled_df_adr['adr'])
plt.plot(canceled_df_adr['reservation_status_date'],canceled_df_adr['adr'])
plt.legend()


# In[134]:


canceled_df_adr[['adr','reservation_status_date']]


# In[135]:


canceled_df_adr=canceled_df_adr[(canceled_df_adr['reservation_status_date']>'2016')& (canceled_df_adr['reservation_status_date']<'2017-09')]
not_canceled_df_adr=not_canceled_df_adr[(not_canceled_df_adr['reservation_status_date']>'2016')& (not_canceled_df_adr['reservation_status_date']<'2017-09')]


# In[155]:


plt.figure(figsize=(20,8))

plt.title('ADR',fontsize=20)

plt.plot(not_canceled_df_adr['reservation_status_date'],not_canceled_df_adr['adr'],label='not_canceled')
plt.plot(canceled_df_adr['reservation_status_date'],canceled_df_adr['adr'],label='canceled')
plt.legend(fontsize=20)
plt.savefig('ana8.png')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:


df.info()


# In[ ]:


df['reservation_status_date']=pd.to_datetime(df['reservation_status_date'],dayfirst=True)


# In[ ]:


df.info()


# In[ ]:


df.describe(include="object")


# In[ ]:


for col in df.describe(include="object").columns:
    print(col)
    print(df[col].unique())
    print('-----'*8)


# In[ ]:


df.isnull().sum()


# In[ ]:


df.drop(['company','agent'],axis=1,inplace=True)


# In[ ]:


df.dropna(inplace=True)


# In[ ]:


df.isnull().sum()


# In[ ]:


df.describe()


# In[ ]:


df['adr'].plot(kind='box')


# In[ ]:


df=df[df['adr']<5000]


# # data analysis & visulizations

# In[ ]:


cancelled_per = df['is_canceled'].value_counts(normalize=True)
print(cancelled_per)

plt.figure(figsize=(5,4))
plt.title('reservation status')
plt.bar(['canelled','not cancelled'],df['is_canceled'].value_counts(),edgecolor='k')
plt.show()


# In[ ]:


plt.figure(figsize=(8,5))
ax1=sns.countplot(x='hotel',hue='is_canceled',data=df,palette='Blues')
plt.legend()
ax1.set_title('Rserveration status in different hotels',size=20)

plt.xlabel('hotel type')
plt.ylabel('Number of reservations')


# In[ ]:


resort_hotel=df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[ ]:


city_hotel=df[df['hotel']=='City Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[ ]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[ ]:


plt.figure(figsize=(20,8))
plt.plot(resort_hotel.index,resort_hotel['adr'],label='resort')
plt.plot(city_hotel.index,city_hotel['adr'],label='city')
plt.title('ADR in city & resort')


# In[ ]:


resort_hotel


# In[ ]:


df['month']=df['reservation_status_date'].dt.month


# In[ ]:


plt.figure(figsize=(16,8))
axes1=sns.countplot(x='month',hue='is_canceled',data=df)
plt.title('month wise rerservation status')
plt.legend(['not can','can'])
plt.xlabel('month')
plt.ylabel('no of rservartions')
plt.show()


# In[ ]:


plt.figure(figsize=(16,8))
dff=df[df['is_canceled']==1].groupby('month')[['adr']].sum().reset_index()
sns.barplot(x='month',y='adr',data=dff)
plt.show()


# In[ ]:


canceled_data =df[df['is_canceled']==1]
top_10_country=canceled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.pie(top_10_country,autopct='%.2f',labels=top_10_country.index)
plt.show()
plt.savefig('names.png')


# In[ ]:


df['market_segment'].value_counts(normalize=True)


# In[ ]:


canceled_data['market_segment'].value_counts(normalize=True)


# In[ ]:


canceled_data_dr=canceled_data.groupby('reservation_status_date')[['adr']].mean()
canceled_data_dr.reset_index(inplace=True)
canceled_data_dr.sort_values('reservation_status_date',inplace=True)

not_canceled_data=df[df['is_canceled']==0]
not_canceled_data_dr=not_canceled_data.groupby('reservation_status_date')[['adr']].mean()
not_canceled_data_dr.reset_index(inplace=True)
not_canceled_data_dr.sort_values('reservation_status_date',inplace=True)
plt.figure(figsize=(18,8))
plt.plot(canceled_data_dr['reservation_status_date'],canceled_data_dr['adr'],label='canceled',color='b')
plt.plot(not_canceled_data_dr['reservation_status_date'],not_canceled_data_dr['adr'],label='not canceled',color='g')
plt.show()


# In[ ]:


canceled_data.head(2)


# In[ ]:


canceled_data_dr=canceled_data_dr[(canceled_data_dr['reservation_status_date']>'2016') & (canceled_data_dr['reservation_status_date']<'2017-09')]
not_canceled_data_dr=not_canceled_data_dr[(not_canceled_data_dr['reservation_status_date']>'2016') & (not_canceled_data_dr['reservation_status_date']<'2017-09')]


# In[ ]:


plt.figure(figsize=(18,8))
plt.plot(canceled_data_dr['reservation_status_date'],canceled_data_dr['adr'],label='canceled',color='b')
plt.plot(not_canceled_data_dr['reservation_status_date'],not_canceled_data_dr['adr'],label='not canceled',color='g')
plt.legend()
plt.savefig('gopal2.png')
plt.show()


# In[150]:


df.to_csv('hotel_bookings 2.csv')


# In[ ]:




