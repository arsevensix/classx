import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# Creating the dataset
data = {
    'Occupants': [2, 4, 3, 2, 5],
    'Appliances': [10, 15, 12, 8, 20],
    'Temperature': [25, 30, 22, 28, 20],
    'EnergyEfficient': [1, 0, 1, 1, 0],
    'EnergyConsumption': [150, 200, 180, 120, 250]
}

df = pd.DataFrame(data)

# Splitting the data into features (X) and target variable (y)
X = df[['Occupants', 'Appliances', 'Temperature', 'EnergyEfficient']]
y = df['EnergyConsumption']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Creating a linear regression model
model = LinearRegression()

# Training the model
model.fit(X_train, y_train)

# Making predictions on the test set
y_pred = model.predict(X_test)

# Calculating metrics
mae = metrics.mean_absolute_error(y_test, y_pred)
mse = metrics.mean_squared_error(y_test, y_pred)

# Displaying the results
print('Mean Absolute Error (MAE):', mae)
print('Mean Squared Error (MSE):', mse)
