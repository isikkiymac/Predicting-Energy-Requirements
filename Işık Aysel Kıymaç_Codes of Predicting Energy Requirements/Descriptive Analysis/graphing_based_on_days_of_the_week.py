import pandas as pd
import matplotlib.pyplot as plt

# Weekly data
weekly_data = pd.DataFrame({
    'day_of_the_week': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'energy_consumption': [181905.5547, 187821.0923, 185887.2, 182959.6615, 181328.0308, 152436.8769,
                           151979.1692]
})

#data visualization
plt.figure(figsize=(12, 6))
plt.plot(weekly_data['day_of_the_week'], weekly_data['energy_consumption'])
plt.xlabel('Days of the Week')
plt.ylabel('Energy Consumption (kWh)')
plt.title('Energy Consumption Based on Days of the Week')
plt.show()
