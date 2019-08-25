import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle

dataset = pd.read_csv("./data/sample_data.csv")
print(dataset["y"].describe())

X = dataset["X"].values.reshape(-1, 1)
y = dataset["y"].values.reshape(-1, 1)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

pickle.dump(regressor, open('../data/model.pkl', 'wb'))

df = pd.DataFrame({"Actual": y_test.flatten(), "Predicted": y_pred.flatten()})
print(df)

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(
    metrics.mean_squared_error(y_test, y_pred)))
