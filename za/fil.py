#
# import os
# import sys
#
# n = 58  # total number of dirs
# path = sys.path.append ( "E:\\新品杂货\\2022年3月\\simm\\" )  # prefix of dir
# for i in range ( 1, n, 1 ):
#     tmp_path = path + str ( i )
#     mkpath = tmp_path + '/'
#     if not os.path.exists ( mkpath ):
#         os.mkdir ( mkpath )
# print ( "done!" )

import os

def mkd():
    path = "E:\\女装新品\\2022\\眼经\\wooden\\" #文件存哪里
    for i in range(2, 200): #创建一个文件并循环20-1次

        k = "%09d" % i # 两位数,不足向前取零

        file_name = path + str(k) #给文件命名 路径+ 文件标号（以标号为名字）

        os.makedirs(file_name)#创建文件

        mkpath = file_name + '/'#路径下钻

        # wenben = open(mkpath + str(k) +".txt", "w") #在上面建的那个文件里边再建一个TXT文件
        #
        # wenben.write("THIS IS " + k + " TEXT")#给TXT里边写点内容

        print(file_name + "创建成功")

        i = i+1

mkd()#函数调用

