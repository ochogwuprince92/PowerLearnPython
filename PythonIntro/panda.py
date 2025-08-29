# Step 0: Import Required Libraries
# Data handling
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Optional: make plots appear inline in Jupyter Notebook
%matplotlib inline

# Task 1: Load and Explore the Dataset
# Load dataset (example: Iris dataset CSV)
try:
    df = pd.read_csv('iris.csv')  # replace 'iris.csv' with your file path
except FileNotFoundError:
    print("Error: File not found. Make sure the CSV file is in the correct location.")
except Exception as e:
    print("Error loading the dataset:", e)

# Inspect the first few rows
print(df.head())

# Check dataset info and data types
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Clean missing values (example: drop rows with missing data)
df = df.dropna()
# or you could fill missing values: df['column_name'].fillna(value, inplace=True)

# Task 2: Basic Data Analysis
# Basic statistics
print(df.describe())

# Example: group by a categorical column and compute mean of a numerical column
grouped = df.groupby('species')['sepal_length'].mean()  # replace 'species' and 'sepal_length' if needed
print(grouped)

# Example: other findings
print("Correlation between numerical columns:")
print(df.corr())

# Task 3: Data Visualization
# 1. Line Chart (trends over a numeric column, simulated index as time)
plt.figure(figsize=(8,5))
plt.plot(df.index, df['sepal_length'], marker='o', linestyle='-', color='b')
plt.title('Sepal Length over Index')
plt.xlabel('Index')
plt.ylabel('Sepal Length')
plt.grid(True)
plt.show()

# 2. Bar Chart (comparison of numerical value across categories)
plt.figure(figsize=(8,5))
sns.barplot(x='species', y='sepal_length', data=df, ci=None)
plt.title('Average Sepal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length')
plt.show()

# 3. Histogram (distribution of a numerical column)
plt.figure(figsize=(8,5))
plt.hist(df['petal_length'], bins=10, color='green', edgecolor='black')
plt.title('Distribution of Petal Length')
plt.xlabel('Petal Length')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot (relationship between two numerical columns)
plt.figure(figsize=(8,5))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df, s=100)
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.legend(title='Species')
plt.show()