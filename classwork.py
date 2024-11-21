import pandas as pd

# data = [3,5,6,8,9]
# series = pd.Series(data)
# print(series)
#
# #датафрейм
# data_f = {
#     "name" : ['Alice', 'Bob', 'Roma', 'Anna'],
#     "age" : [23, 45, 17, 24],
#     "city" : ['New York', 'LA', 'Chicago', 'Moscow']
# }
#
# df = pd.DataFrame(data_f)
# print(df)

df = pd.read_csv('World-happiness-report-2024.csv')
print(df.head()) #в скобках можно ввести число отображаемых строк