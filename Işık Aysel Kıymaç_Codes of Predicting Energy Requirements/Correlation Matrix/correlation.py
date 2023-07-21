import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('hourly_data.csv')

correlation_matrix = df.corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='RdYlBu')
plt.title('Correlation Matrix')
plt.show()
