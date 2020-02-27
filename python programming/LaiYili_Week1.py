# Week 1 - Assessed Exercises
# Fill in the following Python script and submit it on Brightspace.
# An empty line between the question and 'Ans:' implies that you will need to
# write a piece of code to get the answer.

import pandas as pd



# Import Heart Disease UCI data set and call is heart
heart = pd.read_csv('C:/Users/vera/Desktop/DPP/project/heart.csv')
print(heart.dtypes)
# Q1 (a) How many rows and columns there are in the Heart Disease UCI data set?
print(heart.shape)
# Ans: This data set has 303 rows and 14 columns

# Q1 (b) What sex is the 3rd person in the data set, i.e. on the third row?
print(heart[2:3])
# Ans:   age  sex  cp  trestbps  chol  fbs  ...  exang  oldpeak  slope  ca  thal  target
# 2   41    0   1       130   204    0  ...      0      1.4      2   0     2       1
# According to the result,the sex of 3rd person is male

# Compute the table of different chest pain types.
print(pd.pivot_table(heart,'age',index='cp',aggfunc=len,fill_value=0))
# Q2 How many people have type 3 chest pain?
# Ans:23

# Q3 (a) What age is the youngest person in this dataset?
print(heart.age.min())
# Ans:29

# Q3 (b) What age is the oldest person in this dataset?
print(heart.age.max())
# Ans:77

# Look up what the cut function (pd.cut) does and use it to create a new
# variable which is age grouped into 20-30, 30-40, 40-50, 50-60, 60-70, 70-80.
listBins = [20, 30, 40, 50, 60, 70, 80]
listLabels= ['20-30', '30-40', '40-50', '50-60', '60-70', '70-80']
heart['group_age'] = pd.cut(heart.age,listBins,labels=listLabels, include_lowest=True)
# Q4 How many people are in the group (50,60)?
print(heart['group_age'].value_counts())
# Ans:129
