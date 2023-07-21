import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("quadratic_regression_analysis - Sheet1.csv")

plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data["energy_consumption"])
plt.xlabel("Date")
plt.ylabel("Predicted Energy Consumption")
plt.title("Predicted Hourly Energy Consumption by Quadratic Regression")
plt.show()