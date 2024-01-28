# import library
import pandas as pd

# empty dataframe
df = pd.DataFrame()

city = ['Berlin', 'Munich', 'Frankfut']

df = pd.DataFrame(city)
print(df)
print(type(df))

row, col = df.shape
print(row)
print(col)

df = pd.DataFrame(city, index=['c1','c2','c3'] ,columns=['City_in_Europe'])
print(df)

city2 = ['Dortmund', 'Hamburg', 'Potsdom']
df2 = pd.DataFrame(zip(city, city2), columns=['City1', 'City2'])

print(df2)

city3 =[['Bavaria', 'Erlangen'],['NRW','Dortmund']]
df3 = pd.DataFrame(city3, columns=['State','City'])

print(df3)

dict1 = {
    'city1': city,
    'city2': city2
}

df4 = pd.DataFrame(dict1)
print(df4)
