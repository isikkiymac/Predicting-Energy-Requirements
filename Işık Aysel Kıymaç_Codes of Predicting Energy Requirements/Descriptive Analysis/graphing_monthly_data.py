import pandas as pd
import matplotlib.pyplot as plt

# Monthly data
monthly_data = pd.DataFrame({
    'month': ['2018-01', '2018-02', '2018-03', '2018-04', '2018-05', '2018-06', '2018-07',
              '2018-08', '2018-09', '2018-10', '2018-11', '2018-12'],
    'energy_consumption': [4259872.8, 3924540, 4137076.8, 4091198.4, 6008032.8, 6405595.2,
                           6205579.2, 6986512.8, 5969296.8, 5996572.8, 4846701.6, 5015440.8]
})

monthly_data['month'] = pd.to_datetime(monthly_data['month'], format='%Y-%m')

#data visualization
plt.figure(figsize=(12, 6))
plt.plot(monthly_data['month'], monthly_data['energy_consumption'])
plt.xlabel('Month')
plt.ylabel('Energy Consumption (kWh)')
plt.title('Monthly Energy Consumption')
plt.show()
