# import requests
# from bs4 import BeautifulSoup
import pandas as pd
#
# list=[]
# city=['LA ','NY ','MA ','TX ']
# year=['2016','2017','2018', '2019','2020']
#
# for i in city:
#  for j in year:
#    list.append(i+j+".csv")
#
# df=pd.concat([pd.read_csv(i) for i in list])
from functools import reduce
list = ['W223.CSV','33.csv']
list_of_dataframes=[]
for i in list:
    list_of_dataframes.append(pd.read_csv(i))
df_final = reduce(lambda left,right: pd.merge(left,right,on='Title'), list_of_dataframes)
df = pd.DataFrame ( df_final )
# print (df)
df.to_csv ('hawandle.csv')