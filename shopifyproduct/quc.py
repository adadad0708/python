# import csv
# import pandas as pd
#
# data = pd.read_csv ( "44.csv" )  # 读取csv文件
#
# dateMap = []
#
# for i in range ( len ( data ) ):
#     dateMap.append ( data["Option1 Value"][i] )
#
# print ( "去重复前数量：" + len ( data ).__str__ () )
# formatList = list ( set ( dateMap ) )
# formatList.sort ( key=dateMap.index )
#
# print ( "去重复后数量：" + len ( formatList ).__str__ () )
# print(formatList)
import pandas as pd
import glob

outputfile = r'F:\project\pratice\shopifyproduct\csv\hebing.csv'
csv_list = glob.glob ( r'F:\project\pratice\shopifyproduct\csv\*.csv' )
print (csv_list)
print ( '共发现%s个CSV文件' % len ( csv_list ) )
print ( '正在处理' )


def hebing(csv_list):
    for inputfile in csv_list:
        f = open ( inputfile )
        data = pd.read_csv ( f, header=None )
        data.to_csv ( outputfile, mode='a', header=False, index=False )
    print ( '完成合并' )


def quchong(file):
    df = pd.read_csv ( file, header=None )
    print ( df[df.duplicated ()] )  # 打印重复的行
    datalist = df.drop_duplicates ()
    datalist.to_csv ( file )
    print ( '完成去重' )


if __name__ == '__main__':
    hebing ()
    quchong ( outputfile )


# #coding=utf-8
# import os
# import pandas as pd
# import glob
#
#
# def hebing():
#     csv_list = glob.glob('*.csv')
#     print(u'共发现%s个CSV文件'% len(csv_list))
#     print(u'正在处理............')
#     for i in csv_list:
#         fr = open(i,'r').read()
#         with open('haha.csv','a') as f:
#             f.write(fr)
#     print(u'合并完毕！')
#
#
# def quchong(file):
#     df = pd.read_csv(file,header=0)
#     datalist = df.drop_duplicates()
#     datalist.to_csv(file)
#
#
# if __name__ == '__main__':
#     hebing()
#     quchong("haha.csv")