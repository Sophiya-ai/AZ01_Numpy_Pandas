import pandas as pd

df_job = pd.read_csv('data_science_job.csv')
print(df_job.head())
print(df_job.info())
print(df_job.describe())

df_salary = pd.read_csv('dz.csv')
print(df_salary)
df_salary.fillna(0, inplace=True)
print(df_salary)
group = df_salary.groupby('City')['Salary'].mean()
print(group)