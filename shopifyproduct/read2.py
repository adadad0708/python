import pandas as pd

path = 'Option.csv'#读取数据
# df = pd.read_csv(path, encoding='gbk',usecols=[0,4,6])#选取第1，5，7列
# frame = pd.DataFrame(df)
# df2 = df1.drop_duplicates(subset=None, keep='first', inplace=False)
#
# print(frame)
# frame.to_csv ( '00.csv' )
df = pd.read_csv(path, encoding='gbk')
print(df.iloc[1:6,-1:])

