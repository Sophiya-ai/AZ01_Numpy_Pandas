import pandas as pd

df = pd.read_csv('animal.csv')
print(df)

#замена значений NaN на какое-либо другое, 0 например,
# fillna заполняет все пропуски
#df.fillna(0, inplace=True)
#print(df)

#Если не хотим заменять значения, можно их удалить,
# хотя это всё-таки делать не рекомендуется
#df.dropna(inplace=True)
#print(df)

#группировка по значениям в столбце Пища и вычислим ср продолжит жизни по группе каждой
group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
print(group)
