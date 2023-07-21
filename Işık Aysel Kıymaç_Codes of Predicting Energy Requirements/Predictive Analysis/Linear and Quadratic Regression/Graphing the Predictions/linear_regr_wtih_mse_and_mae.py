import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error


#data from CSV files
data1 = pd.read_csv('linear_regression_analysis - Sheet1.csv')  
data2 = pd.read_csv('hourly_data.csv')  

x1 = data1['Date']
y1 = data1['energy_consumption']

x2 = data2['Date']
y2 = data2['energy_consumption']

y1 = y1.fillna(y1.mean())
y2 = y2.fillna(y2.mean())

plt.figure(figsize=(12, 6))

plt.plot(x1, y1, label='Linear Regression')

plt.plot(x2, y2, label='Hourly Energy Consumption')

#labels and title
plt.xlabel('Date')
plt.ylabel('Energy Consumption')
plt.title('Comparison of Hourly Energy Consumption and Predicted Energy Consumption by Linear Regression')

#mean squared error
mse = np.mean((y1 - y2) ** 2)

mse_annotation = f'MSE: {mse:.4f}'

#mean absolute error
mae = mean_absolute_error(y1, y2)

plt.text(0.5, 0.9, f'MAE: {mae:.4f}', transform=plt.gca().transAxes)

plt.annotate(mse_annotation, (0.5, 0.95), xycoords='axes fraction')

plt.legend()

plt.show()
