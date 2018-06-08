#coding:utf-8
import pandas as pd
# import numpy as np

# 读取csv文件
name = ["A","B","C"]
df = pd.read_csv(r"barcode.csv",encoding="utf-8",names=name)
print(df['C'])
# df.reindex
df['N8'] = df['N7']=df['N6']=df['N5']=df['N4']=df['N3']=df['N2']=df['N1']=None
lis = []
count = 0

for i in df.index:
    lis.append(df['C'][i])
# print(lis,type(lis))
for i in range(len(lis)):
    arr = lis[i]
# print(arr[0])
    N8 = N7 = N6 = N5 = N4 = N3 = N2 = N1 = 0
    for j in range(len(lis)):
        # pass
        # print(arr[])
        if lis[j][0] ==arr[0]:
            N8 =1
        if arr[1] == lis[j][1]:
            N7 =1
        if arr[2] == lis[j][2]:
            N6 =1
        if arr[3] == lis[j][3]:
            N5 =1
        if arr[4] == lis[j][4]:
            N4 = 1
        if arr[5] == lis[j][5]:
            N3 = 1
        if arr[6] == lis[j][6]:
            N2 = 1
        if arr[7] == lis[j][7]:
            N1 = 1
            sum = N1+N2+N3+N4+N5+N6+N7+N8
            print(sum)
        M1=M2=M3=M4=M5=M6=M7=M8=0
        # if sum == 8:

            # if N1+N2+N3+N4+N5+N6+N7+N8 == 8:
            #     df['N8'][i] =
        # df['N8'][i] = N8
        # df['N7'][i] = N7
        # df['N6'][i] = N6
        # df['N5'][i] = N5
        # df['N4'][i] = N4
        # df['N3'][i] = N3
        # df['N2'][i] = N2
        # df['N1'][i] = N1
        # # df['N6'][i] = N6
    # print(N8,N7,N6,N5,N4,N3,N2,N1)
# writer = pd.ExcelWriter("barcode.xlsx")
# df.to_excel(writer,index=False)
# writer.save()
# print(df.select)

# 随机生成 TAGC组成的8位字符串
