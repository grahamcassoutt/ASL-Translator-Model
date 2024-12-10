# asl-model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import coremltools as ct


df = pd.read_excel('positions2.xlsx', sheet_name='Sheet1')

# Get data for inputs and outputs
x = df.iloc[:, 0:40].values
y = df.iloc[:, 40].values

# Splits into train and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)


lr = LogisticRegression(multi_class='ovr', max_iter=200)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

# Printing and Saving
print("Accuracy:", accuracy)
coremlModel = ct.converters.sklearn.convert(
    lr,
    input_features=[f"feature_{i}" for i in range(1, 41)],
    output_feature_names="label"
)
coremlModel.save("PositionsLogisticRegression4.mlmodel")


