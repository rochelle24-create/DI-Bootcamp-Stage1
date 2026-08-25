# Daily Challenge: Data Handling and Analysis in Python


# What You Will Learn
# Advanced techniques for data normalization, reduction, and aggregation.
# Skills in gathering, exploring, integrating, and cleaning data using Python.
# Proficiency in using Pandas for complex data manipulation.


# Your Task
# Download and import the Data Science Job Salary dataset.
# Normalize the ‘salary’ column using Min-Max normalization which scales all salary values between 0 and 1.
# Implement dimensionality reduction like Principal Component Analysis (PCA) or t-SNE to reduce the number of features (columns) in the dataset.
# Group the dataset by the ‘experience_level’ column and calculate the average and median salary for each experience level (e.g., Junior, Mid-level, Senior).
# Hint :
# As a reminder, normalization is crucial when dealing with data that has different ranges. For example, salary data might have a wide range (e.g., from $20,000 to $200,000). By scaling the data using Min-Max normalization, you make sure that all salary values fall within a consistent range (0 to 1). This is particularly helpful when the data is going to be used in machine learning models, as some algorithms (like k-nearest neighbors or neural networks) perform better when features are normalized. It ensures that no single salary dominates the learning process, making the analysis more balanced.

# Dimensionality reduction helps simplify complex datasets by reducing the number of variables under consideration. This can make the data more manageable and help avoid the curse of dimensionality—a phenomenon where machine learning models struggle when dealing with high-dimensional data.
# PCA, for instance, helps in retaining the most important information (variance) from the dataset while reducing noise and redundancy.
# It can also speed up the training process for models and help in visualizing data in fewer dimensions.

# Aggregating data helps in understanding trends within subgroups of the dataset.
# Calculating average and median salaries for each experience level gives insights into the compensation distribution and disparities across different job levels. This kind of aggregation can help in answering business questions like “How does salary evolve with experience?” or “What is the salary distribution for senior-level roles?”

from pathlib import Path

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

# Load dataset (sits next to this script)
CSV_PATH = Path(__file__).parent / 'datascience_salaries.csv'

df = pd.read_csv(CSV_PATH, index_col=0)
df.info()

# 1. Min-Max Normalization of salary column
scaler = MinMaxScaler(feature_range=(0, 1))
df['salary_normalized'] = scaler.fit_transform(df[['salary']])

# 2. Dimensionality Reduction with PCA
df_encoded = pd.get_dummies(df, columns=['job_title', 'job_type', 'experience_level', 'location', 'salary_currency'])
df_encoded = df_encoded.astype(int)
X = df_encoded.select_dtypes(include=[np.number]).drop('salary', axis=1)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print(f'PCA: {X.shape[1]} features -> {X_pca.shape[1]} components')
print('Explained variance ratio:', pca.explained_variance_ratio_.round(4))
print()

# 3. Group by experience_level and calculate average and median salary
salary_stats = df.groupby('experience_level')['salary'].agg(['mean', 'median']).round(2)
print(salary_stats)


