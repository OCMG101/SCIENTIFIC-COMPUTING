import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\Oliver\Documents\Schoolwork\2.2\SCIENTIFIC COPMUTING\sample_data.csv.xls")
print(data)

data.info()

print(data[["temperature", "humidity"]])

high_temp = data[data["temperature"]>26]

print(high_temp)

print(data.loc[data["category"] == 'Science', ["temperature", "humidity"]])

print(data.iloc[0:4,0:3])

print(data.loc[data["temperature"]>25])

# Basic Statistics

print(data["temperature"].mean())
print(data["temperature"].median())
print(data["temperature"].std())


# DATA VISUALISATION

data["temperature"].hist(bins=5)
plt.show()

# HANDLING OUTLIERS

# Identifying and removing outliers using the interquartile range

Q1 = data["temperature"].quantile(0.25)
Q3 = data["temperature"].quantile(0.75)
IQR = Q3 - Q1

data_no_outliers = data[(data["temperature"] >= (Q1 - 1.5 * IQR)) &
                        (data["temperature"] <= (Q3 + 1.5 * IQR))]

print(data_no_outliers)

# NORMALIZING AND TRANSFORMING DATA

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

print(scaler)

