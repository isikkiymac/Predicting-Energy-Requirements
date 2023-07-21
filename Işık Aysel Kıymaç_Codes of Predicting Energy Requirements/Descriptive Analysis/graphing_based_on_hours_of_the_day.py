import pandas as pd
import matplotlib.pyplot as plt

hour_data = pd.DataFrame({
    'hour': ['0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00',
              '7:00', '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
    'energy_consumption': [6328.280548, 6265.939726, 6228.558904, 6206.761644, 6376.668493, 6532.280548,
                           7587.281096, 7901.010411, 7972.550137, 8088.190685, 8209.762192, 8290.428493, 8341.913425, 8371.443288, 8385.073973, 8325.284384, 8167.943014, 7718.169863, 6969.646027, 6698.294795, 6592.8, 6421.959452, 6488.981918, 6452.475616]
})

#data visualization
plt.figure(figsize=(12, 6))
plt.plot(hour_data['hour'], hour_data['energy_consumption'])
plt.xlabel('Hours of the Day')
plt.ylabel('Energy Consumption (kWh)')
plt.title('Energy Consumption Based on Hours of the Day')
plt.show()
