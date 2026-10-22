import numpy as np 
import pandas as pd  

arr = np.array([1,2,3,4,5])
sr = pd.Series([1,2,3,4,])
sr2 = pd.Series(arr)
df = pd.DataFrame(arr, columns = ['col1'], index = ['ek', 'do', 'teen', 'char', 'panch'])

# EDA of Iris dataset: 01
iris = pd.read_csv('D:/Code Field Offline/datasets/iris.csv')
# print(iris)
# print(iris.head())
# print()
# print(iris.tail())
# print()
# print(iris.describe())
# print()
# print(iris.info())
# print()
# print(iris.shape)
# print()
# print(iris.columns)
# print()
# print(iris.index)

def eda(location):
	df = pd.read_csv(location)
	print('welcome to exploratory dataset analysis (eda)'.upper())
	print(f'>>> dataset: '.title(), location)
	print(df, '\n\n')
	print('>>> First five entries: '.title())
	print(df.head(), '\n\n')
	print('>>> Last five entries: '.title())
	print(df.tail(), '\n\n')
	print('>>> Statastical information: '.title())
	print(df.describe(), '\n\n')
	print('>>> General information: '.title())
	print(df.info(), '\n\n')
	print('>>> Shape: '.title())
	print(df.shape, '\n\n')
	print('>>> Columns: '.title())
	print(df.columns, '\n\n')
	print('>>> Index: '.title())
	print(df.index, '\n\n')

iris = 'D:/Code Field Offline/datasets/iris.csv'
penguins = 'D:/Code Field Offline/datasets/penguins.csv' # this set has some missing values (in bill lenght, bill depth, flipper lenght, body mass, sex)
tips = 'D:/Code Field Offline/datasets/tips.csv'
titanic = 'D:/Code Field Offline/datasets/titanic.csv' # this set has soem missing values (in age, cabin, embarked)

eda(penguins)

# this follwing is very special one 
df = pd.read_csv(titanic)
print(df.columns)
print(df['Sex'].value_counts()) # this is also important