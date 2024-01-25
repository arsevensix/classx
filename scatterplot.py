import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the dataset
data = {
    'Occupants': [2, 4, 3, 2, 5],
    'Appliances': [10, 15, 12, 8, 20],
    'Temperature': [25, 30, 22, 28, 20],
    'EnergyEfficient': [1, 0, 1, 1, 0],
    'EnergyConsumption': [150, 200, 180, 120, 250]
}

df = pd.DataFrame(data)

# Scatter plot: Number of Occupants vs Energy Consumption
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Occupants', y='EnergyConsumption', data=df, color='blue')
plt.title('Number of Occupants vs Energy Consumption')
plt.xlabel('Number of Occupants')
plt.ylabel('Energy Consumption')
plt.show()

# Scatter plot: Appliances vs Energy Consumption
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Appliances', y='EnergyConsumption', data=df, color='green')
plt.title('Appliances vs Energy Consumption')
plt.xlabel('Number of Appliances')
plt.ylabel('Energy Consumption')
plt.show()

# Scatter plot: Temperature vs Energy Consumption
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Temperature', y='EnergyConsumption', data=df, color='orange')
plt.title('Temperature vs Energy Consumption')
plt.xlabel('Average Daily Temperature')
plt.ylabel('Energy Consumption')
plt.show()

# Scatter plot: Energy Efficient Measures vs Energy Consumption
plt.figure(figsize=(8, 6))
sns.scatterplot(x='EnergyEfficient', y='EnergyConsumption', data=df, color='red')
plt.title('Energy Efficient Measures vs Energy Consumption')
plt.xlabel('Energy Efficient (1: Yes, 0: No)')
plt.ylabel('Energy Consumption')
plt.show()
