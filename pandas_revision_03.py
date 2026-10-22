# data selection and filtering and cleaning and preprocessing data

import pandas as pd  

df = pd.read_csv('D:/Code Field Offline/datasets/bollywood.csv')

print(df)

# selection

print(df.loc[8])

print(df['Actor'])

print(df[['Film', 'Year']])

print(df.loc[[1,2,3],['IMDb', 'Genre']])

print(df.iloc[4:7,2:4]) # let a:b so iloc do not take the last b it takes b-1 so a:b-1

print(df.at[9, 'Year']) # fast accase elements not for sclicing

print(df.iat[9, 2])

# filtering

print(df[df['IMDb'] > 7])

print(df[df['Genre'] == 'Action'])

print(df[(df['IMDb'] > 7) & (df['Genre'] == 'Action')])

# there is one more thing callad .query similar to sql quresy cover later

# Data Cleaning (removing managing missing and duplicated values/rows/columns)

penguins = 'D:/Code Field Offline/datasets/penguins.csv'
df = pd.read_csv(penguins)
# NOTE: to understand this part easly focus on the index 3 in the output table becuase it has NaN values which you an identify easly 
print(df)
print()
print(df.columns)

# finding null values: 

print(df.isnull())
print(df.isnull().sum())

# droping (removing) null values:

print(df.dropna()) # this drops all the null 'rows'
# as you can see the no of rows has dicreasies
print(df.info())
print(df.dropna().info())

print(df.dropna(axis=1)) # this drops all the null 'columns'
# as you can see the no of columns has dicreasees
print(df.info())
print(df.dropna(axis=1).info())

# filling null values

# this is direct fill
print(df.fillna(0)) # this is fill the missing space with 0

# this is conditional fill 
# so sometimes we'll just let that the missing values are the avarage of the rest of the values in that particluar column
# for example in this will have missing value in body mass of the penguins so will can replace the missing values with the avarage of the rest of the data in the column, here how will do this
print(df['body_mass_g'].fillna(df['body_mass_g'].mean()))
# in this we used mean but you can also give any condition like max or min or any other( this is the most common use case )

# we can also fill the missing value with the just next value and with just before value

print(df.ffill()) # this will fill value from the next non missing value

print(df.bfill()) # this will fill value from the before non missing value
# Duplicated values

df = pd.read_csv('D:/Code Field Offline/datasets/duplicated.csv')

print(df)
# to find duplicated values
print(df.duplicated())

# to drop (revmove) duplicated rows
print(df.drop_duplicates()) 

# to check duplicated value in spific column
print(df.duplicated(subset=['Gender']))
print(df.duplicated(subset=['Join Date', 'Age'])) # multiple columns as once

# lets test droping duplicates in large dataset 
a = pd.read_csv('D:/Code Field Offline/datasets/tips.csv')
print(a.shape)
print(a.drop_duplicates().shape)
# so as yo can see tthis as only one duplicated row

# Data Pre Processing (playing with stings mthods ,appplying fuction, type casting etc)

# so data pre prossessing is in next file that pandas_revision_04.ipynb