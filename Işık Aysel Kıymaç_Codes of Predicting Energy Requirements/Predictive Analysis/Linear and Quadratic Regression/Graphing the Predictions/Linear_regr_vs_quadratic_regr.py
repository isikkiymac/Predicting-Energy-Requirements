import matplotlib.pyplot as plt
import pandas as pd

#data from CSV files
data1 = pd.read_csv('linear_regression_analysis - Sheet1.csv')
data2 = pd.read_csv('quadratic_regression_analysis - Sheet1.csv') 

x1 = data1['Date']
y1 = data1['energy_consumption']

x2 = data2['Date']
y2 = data2['energy_consumption']

plt.figure(figsize=(12, 6))

plt.plot(x1, y1, label='Linear Regression')

plt.plot(x2, y2, label='Quadratic Regression')

#labels and title
plt.xlabel('Date')
plt.ylabel('Predicted Energy Consumption')
plt.title('Comparison of Linear Regression and Quadratic Regression')

plt.legend()

plt.show()
