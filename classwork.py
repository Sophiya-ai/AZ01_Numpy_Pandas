import pandas as pd

# data = [3,5,6,8,9]
# series = pd.Series(data)
# print(series)
#
#датафрейм
data_f = {
    "name" : ['Alice', 'Bob', 'Roma', 'Anna'],
    "age" : [23, 45, 17, 24],
    "city" : ['New York', 'LA', 'Chicago', 'Moscow']
}
df = pd.DataFrame(data_f)
#сохранение в файл
df.to_csv('output.csv', index=False)
#
# df = pd.DataFrame(data_f)
# print(df)

#df = pd.read_csv('World-happiness-report-2024.csv')
#вывод 1ых 5 строк - в скобках можно ввести число отображаемых строк; df.tail() - вывод последних пяти строк
#print(df.head())

#названия всех столбцов и какое количество столбцов содержит в себе информацию,
# а также тип хранящихся данных, сколько памяти тратится
#print(df.info())

#функция позволяет получить статистические данные: найти минимальные,
# максимальные и средние значения, количество и т.д.
#print(df.describe())

#вывод значений какого-то столбца
#print(df['Country name'])

#вывод столбцов
#print(df[['Country name','Regional indicator']])

#вывод данных по объекту (т.е. строки какой-то вывод)
#print(df.loc[56])

#вывод данных по объекту не по индексу, а если нужна часть данных по нему
#print(df.loc[56, 'Healthy life expectancy'])

#вывод по условию
#print(df[df['Healthy life expectancy'] > 0.7])

# df = pd.read_csv('hh.csv')
#
# df['Test'] = [new for new in range(7)]#
# print(df)

# удаление столбка axis=1 или строки axis=0; inplace нужен, чтобы показывать, что изменения,
# которые мы вносим, должны быть внесены в исходный датафрейм
# — в этом случае для этого параметра прописывается значение True.
# В случае, если значение этого параметра False, оригинальный датафрейм останется неизменным
# df.drop('Test', axis=1, inplace=True)
# print(df)
#
# df.drop([0], axis=0, inplace=True)
# print(df)