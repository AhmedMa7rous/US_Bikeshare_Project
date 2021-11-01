import pandas as p

df = p.read_csv('csv_files/chicago.csv')

df_shape = df.shape
print(df_shape[0],'\n',df_shape[1])

df_types = df.dtypes
print(df_types)


df_info = df.inf()
print(df_info)



df_unique = df.nunique()
print(df_unique)

print(df.head(2))
mean_age = df['Age'].mean()






