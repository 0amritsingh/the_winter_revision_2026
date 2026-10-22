import pandas as pd  
import numpy as np
s = pd.Series([1,2,3,4,5], index= ['one', 'two', 'there', 'four', 'five'])
## dataframe using dict
df = pd.DataFrame({
	'name': ['amrit', 'rohan', 'raj'],
	'age': [19, 43, 22], 
	'crush': ['vanshika', 'loda', 'lassun']
	})
# print(type(s), type(df))

# dataframe using list of lists
lst = [['amrit', 19, 'vanshika'], ['rohan', 43, 'loda'], ['raj', 22, 'lassun']]
a = pd.DataFrame(lst)
b = pd.DataFrame(lst, columns = ['name', 'age', 'crush'])
# print(b)

#dataframe using numpy array
arr = np.array([[34, 22], [56, 32]])
a = pd.DataFrame(arr, columns = ['column1', 'column2'], index = ['index1', 'index2'])
# print(a)

# there are also multiple ways to make dataframes like using excel sheet, csv, json
# you can use the following:
# a = pd.read_excel('file location')
# b = pd.read_csv('file location')
# c = pd.read_json('file loctaion')

# EDA (EXPLORATORY DATA ANALYSIS)
df = pd.read_csv('datasets/tips.csv')
# print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.index)