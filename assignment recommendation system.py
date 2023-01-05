# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 13:44:58 2022

@author: vaishnav
"""
#=======================================================================================================================
#importing the data

import pandas as pd

df = pd.read_csv(r"C:\anaconda\New folder\book.csv",encoding='latin1')
df


df.drop(columns=('Unnamed: 0'),axis=1,inplace=True)#dropping unrequired columns



df.rename(columns={'User.ID':'UserID',#renaming column names
                   "Book.Title":"BookTitle",
                   "Book.Rating":"BookRating"},inplace=True)

df.head()

df.info()

df.describe()

df.isnull().any()
#=======================================================================================================================
len(df)

df.sort_values('UserID')
len(df.UserID.unique())

df.BookRating.value_counts().plot(kind='bar')

df['BookRating'].hist()

df.BookTitle.value_counts()

#=======================================================================================================================

# Use Pivot Table to reshape the data
User_df = df.pivot_table(index ='UserID', columns='BookTitle', values='BookRating')
print(User_df)


User_df.fillna(0, inplace=True) #replacing null values with 0
User_df

#=======================================================================================================================

from sklearn.metrics import pairwise_distances
user_sim = 1 - pairwise_distances(User_df.values,metric = 'cosine')
user_sim


user_sim_df = pd.DataFrame(user_sim)

# Set the index and column names to user ids 
user_sim_df.index   = df.UserID.unique()
user_sim_df.columns = df.UserID.unique()

user_sim_df


user_sim_df.iloc[:5,:5]

#=======================================================================================================================

import numpy as np
np.fill_diagonal(user_sim, 0)
user_sim_df.iloc[0:7, 0:7]

# To save your cosin calcutaion file
#user_sim_df.to_csv("cosin_calc.csv")

# Most Similar Users
user_sim_df.max()
user_sim_df.idxmax(axis=1)[0:10]

#=======================================================================================================================

df[(df['UserID'] == 276729) | (df['UserID'] == 276726)]

# System will recommend 'Classical Mythology' to 276729 and 'Decision in Normandy' & 'Clara Callan' to276726
user_1 = df[df['UserID'] == 276729]
user_2 = df[df['UserID']  == 276726]

pd.merge(user_1,user_2,on='BookTitle',how='inner')
pd.merge(user_1,user_2,on='BookTitle',how='outer')

#=======================================================================================================================

df[(df['UserID'] == 276736) | (df['UserID'] == 276726)]

# System will recommend 'Classical Mythology' to 276736 and 'Flu: The Story of the Great Influenza Pandemic' to 276726


user_1 = df[df['UserID'] == 276736]
user_2 = df[df['UserID']  == 276726]


pd.merge(user_1,user_2,on='BookTitle', how='inner')
pd.merge(user_1,user_2,on='BookTitle',how='outer')

#=======================================================================================================================

df[(df['UserID'] == 276744) | (df['UserID'] == 276726)]

# System will recommend 'Classical Mythology' to 276744 and 'The Kitchen God's Wife' & to276726
user_1 = df[df['UserID'] == 276744]
user_2 = df[df['UserID']  == 276726]

pd.merge(user_1,user_2,on='BookTitle', how='inner')
pd.merge(user_1,user_2,on='BookTitle',how='outer')

#==========================================================================================================

df[(df['UserID'] == 276754) | (df['UserID'] == 276726)]

# System will recommend 'Classical Mythology' to 276754 and 'A Second Chicken Soup for the Woman's Soul' to 276726
user_1 = df[df['UserID'] == 276754]
user_2 = df[df['UserID']  == 276726]

pd.merge(user_1,user_2,on='BookTitle', how='inner')
pd.merge(user_1,user_2,on='BookTitle',how='outer')


#==========================================================================================================

df[(df['UserID'] == 276745) | (df['UserID'] == 276726)]

# System will recommend 'Classical Mythology' to 276745 and 'What If?: The World's Foremost Military Histor' to 276726
user_1 = df[df['UserID'] == 276745]
user_2 = df[df['UserID']  == 276726]

pd.merge(user_1,user_2,on='BookTitle', how='inner')
pd.merge(user_1,user_2,on='BookTitle',how='outer')

#==========================================================================================================











