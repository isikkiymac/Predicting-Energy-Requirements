import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

#the dataset
data = pd.read_csv("hourly_data.csv")

numeric_columns = ["Temperature", "Humidity", "energy_consumption"]
numeric_data = data[numeric_columns]

imputer = SimpleImputer(strategy="mean")
imputed_data = imputer.fit_transform(numeric_data)

X = imputed_data[:, :2]  
y = imputed_data[:, 2]   

# Scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)

#linear regression model
linear_model = LinearRegression()
linear_model.fit(X, y)

y_pred_linear = linear_model.predict(X)

#quadratic regression by polynomial features
quadratic_features = PolynomialFeatures(degree=2)
X_quad = quadratic_features.fit_transform(X)

#quadratic regression model
quadratic_model = LinearRegression()
quadratic_model.fit(X_quad, y)

y_pred_quad = quadratic_model.predict(X_quad)

linear_pred_df = pd.DataFrame({'Predicted Energy Consumption (Linear Regression)': y_pred_linear})
quadratic_pred_df = pd.DataFrame({'Predicted Energy Consumption (Quadratic Regression)': y_pred_quad})

linear_pred_df.to_csv('linear_predictions.csv', index=False)
quadratic_pred_df.to_csv('quadratic_predictions.csv', index=False)
