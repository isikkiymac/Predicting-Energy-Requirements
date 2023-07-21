import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("daily_data.csv")

# Visualize energy consumption
plt.figure(figsize=(12, 6))
plt.plot(data["date"], data["energy_consumption"])
plt.xlabel("")
plt.ylabel("Energy Consumption (kWh)")
plt.title("Daily Energy Consumption")
plt.show()
