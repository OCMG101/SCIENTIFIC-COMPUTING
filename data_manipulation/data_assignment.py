#%% md
# # DATA MANIPULATION - ASSIGNMENT
#%%
import pandas as pd
#%%
data = pd.read_csv(r"C:\Users\Oliver\Downloads\Mobile Dataset\Flipkart_Mobiles.csv")
data
#%%
data.info(), data.head()
#%%
data[["Selling Price", "Original Price"]] = data[["Original Price", "Selling Price"]] # Swapping the "Selling Price" and the "Original Price" since they appear to have been wrongly labelled.
data

#%% md
# ## Computing Basic Statistics
#%% md
# - Mean and Median only calculated for "Rating", "Selling Price" and "Original Price" since they are entirely integer values.
#%%
data["Memory"].mode()
#%%
data["Storage"].mode()
#%%
data["Rating"].mean()
#%%
data["Rating"].mode()
#%%
data["Rating"].median()
#%%
data["Selling Price"].mean()
#%%
data["Selling Price"].mode()
#%%
data["Selling Price"].median()
#%%
data["Original Price"].mean()
#%%
data["Original Price"].median()
#%%
data["Original Price"].mode()
#%%
data["Brand"].mode()
#%%
data["Color"].mode()
#%% md
# ## Handling Missing Values
#%%
data.isnull().values.any() # Check for missing values
#%%
data.isnull().sum().sum() # Total number of missing values
#%%
data[data.isnull().any(axis=1)] # Show rows with missing values
#%% md
# - Fill missing "Memory" & "Storage" values with mode and "Rating" values with median
#%%
data["Memory"].fillna(data["Memory"].mode()[0], inplace=True)
data["Storage"].fillna(data["Storage"].mode()[0], inplace=True)
#%%
data["Rating"].fillna(data["Rating"].median(), inplace=True)
#%%
data.isnull().values.any() # Checking whether the missing values have been handled
#%% md
# ## Handling Outliers:
# 
#%%
Q1 = data["Selling Price"].quantile(0.25)
Q3 = data["Selling Price"].quantile(0.75)
IQR = Q3 - Q1

data_no_outliers = data[(data["Selling Price"] >= (Q1 - 1.5 * IQR)) &
                        (data["Selling Price"] <= (Q3 + 1.5 * IQR))]

data_no_outliers
#%% md
# ## Other Computations:
# 
# 
#%%
# Profit made by each company
data["Profit"] = data["Selling Price"] - data["Original Price"]
company_profits = data.groupby("Brand")["Profit"].sum().reset_index()
company_profits = company_profits.sort_values(by="Profit", ascending=False)
company_profits
#%% md
# - It is seen that Samsung made the most profit, Google Pixel made the least profit and HTC made no profit.
#%% md
# ## Data Visualization
# 
# 
#%%
import matplotlib.pyplot as plt
import seaborn as sns
#%%
sns.histplot(data["Selling Price"], bins=30, kde=True).set_title("Histogram Showing the Distribution of Selling Price, Original Price, and Rating") # s
#%%
sns.boxplot(x=data["Selling Price"]).set_title("Boxplot of Selling Price Before Outlier Handling")
#%%
sns.boxplot(x=data_no_outliers["Selling Price"]).set_title("Boxplot of Selling Price After Outlier Handling")
#%%
(data.groupby("Brand")["Selling Price"].mean().sort_values().plot(kind="bar")
.set_title("Bar Chart Comparing the Average Price of Different Brands"))
#%%
(data.groupby("Brand")["Profit"].sum().sort_values(ascending=False).plot(kind="bar")
 .set_title("Bar Chart Comparing the Total Profit for Different Brands"))