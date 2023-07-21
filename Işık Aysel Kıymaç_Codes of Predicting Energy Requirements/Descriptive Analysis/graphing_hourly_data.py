import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("hourly_data.csv")

# Visualize energy consumption
plt.figure(figsize=(12, 6))
plt.plot(data["Date"], data["energy_consumption"])
plt.xlabel("Date")
plt.ylabel("Energy Consumption")
plt.title("Hourly Energy Consumption")
plt.show()


