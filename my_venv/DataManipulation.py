# importing pandas
import pandas as pd

# importing excel file
df = pd.read_csv('Daffodil_Cource_List.csv')

print(df.values)
print(df.columns)
print(df[["Course Code"]])
print(df[["Course Code","Course Title"]].head(5))
print(df['Course Credit'].sort_values())
print(df.describe())
