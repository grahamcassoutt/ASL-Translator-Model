# asl-model.py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import joblib

df = pd.read_excel('asl-alphabet.xlsx', sheet_name='Sheet1')

# Get data for inputs and outputs
x = np.array(df[df.columns[0:16]])
y = np.array(df[df.columns[16]])


# Splits into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

# Train the linear regression model and predict
lr = LinearRegression()
lr.fit(x_train, y_train)
y_predictions = lr.predict(x_test)

joblib.dump(lr, 'asl_linear_regression_model.joblib')

# Printing
y_predictions = np.round(y_predictions, 2)
for i in range(0, len(y_predictions), 1):
    print(i, ' \t', y_test[i], '\t', y_predictions[i])


print('\nR-squared: %.4f' %lr.score(x_test, y_test))
