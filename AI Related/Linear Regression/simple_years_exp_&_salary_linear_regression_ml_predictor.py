# -*- coding: utf-8 -*-
"""Simple Years Exp. & Salary Linear Regression ML Predictor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1218GXknh11ULK92uQOXhILIDZ2zIfoMh
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import scipy
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error, r2_score
# %matplotlib inline

data=pd.read_csv('/content/Salary_dataset.csv')
data.head()

data_cleaned=data.drop(['Unnamed: 0'],axis=1)
data_cleaned.head()

data_cleaned.info()

data_cleaned.describe()

#Declaring the DV and IV
y=data_cleaned['Salary']
x1=data_cleaned['YearsExperience']

#Create a scatter plot that serve as a visual representation of Years Experience in relation to Salary
plt.scatter(x1,y)
plt.xlabel('Years of Experience', fontsize=10)
plt.ylabel('Salary', fontsize=10)
plt.show()

#Getting stats summary by using statsmodel
x=sm.add_constant(x1)

results=sm.OLS(y,x).fit()

results.summary()

#In this case, the constant value is 2.485e+04 (which is in scientific notation, equivalent to 24850)
#The coefficient for "YearsExperience" is 9449.9623

# Extracting constant and coefficient values
constant = results.params[0]
coefficient_years_experience = results.params[1]

print('Constant:', constant.round(2))
print('Coefficient:', coefficient_years_experience.round(2))

#Scatter plot with line of best fit and constant added
plt.scatter(x1,y)
y_hat=constant+coefficient_years_experience*x1
fig=plt.plot(x1,y_hat,lw=5,c='green',label='regression line')
plt.xlabel('Years Experience')
plt.ylabel('Salary')

#Train the model by using linear regression

X=x1
Y=y

X=X.values.reshape(-1,1)

#splitting the data into train and test
X_train, X_test, y_train, y_test=train_test_split(X,Y,test_size=.25)

model=LinearRegression()
model.fit(X_train,y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

#compare the y_pred with the actual y value to see how the prediction did
y_pred

# Create Series from the arrays y and y_pred, resetting the index or else it might lead to not aligning indices from concat
y_series = pd.Series(y_test, name='Original Value').reset_index(drop=True)
y_pred_series = pd.Series(y_pred, name='Predicted Value').reset_index(drop=True)

# Create a DataFrame by concatenating the Series
df_comparison = pd.concat([y_series, y_pred_series], axis=1)

# Calculate the difference between the original and predicted values
df_comparison['Difference'] = df_comparison['Original Value'] - df_comparison['Predicted Value']

# Display the DataFrame
print(df_comparison)

# Evaluate model performance
mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse.round(2))
print("R-squared:", r_squared.round(2))

#Predict Salary based on Years of Experience
experience=[[5]]
predicted_salary=model.predict(experience)
print("Predicted salary given the years of experience: ", predicted_salary)

experiences=[[4],[3],[1],[5],[2]]
salaries_predicted=model.predict(experiences)


df_predictions=pd.DataFrame(
    {
        "Years of experience: ": experiences,
        "Salaries: ": salaries_predicted.round(2)
    }
)

#print("Predicted salaries: ",salaries_predicted)

print(df_predictions)

