#coding:utf-8

import os;

def Capitalize(path):
    i = 0
    j=0
    lis=[]
    # path = ""
    Key=open('defaultValue.txt').read().split('\n')
    defaultValue=open('keys.txt').read().split('\n')
    # print(Key)
    # print(defaultValue)

    # 遍历文件夹下的所有文件和文件夹
    fileList = os.listdir(path)

    for files in fileList:
        # i+=1
        # 旧的文件和文件夹路径
        OldDir = os.path.join(files)
        # if os.path.isdir(OldDir):
        aa = 0;
        for i in defaultValue:
            print(i)
            # print(i)
            aa+=1;
            if OldDir == i:
                print(OldDir)
                # dirname=os.path.splitext(files)[0]  #文件名
                # filetype=os.path.splitext(files)[1]  #文件后缀名
                NewName = os.path.join(path,Key[aa])
                OldName = os.path.join(path,OldDir)
                NewDir = os.rename(OldName,NewName)
        # return NewDir

def LowerCase(path):
    i = 0
    # path = ""
    defaultValue=open('defaultValue.txt').read().split('\n')
    Key=open('keys.txt').read().split('\n')
    # print(Key)
    # print(defaultValue)

    # 遍历文件夹下的所有文件和文件夹
    fileList = os.listdir(path)
    for files in fileList:
        # i+=1
        # 旧的文件和文件夹路径
        OldDir = os.path.join(files)
        # for a in OldDir:
            # if os.path.isdir(OldDir):
        aa = 0;
        for i in defaultValue:
            # print(i)
            aa+=1;
            if OldDir == i:
                print(OldDir)
                # dirname=os.path.splitext(files)[0]  #文件名
                # filetype=os.path.splitext(files)[1]  #文件后缀名
                NewName = os.path.join(path,Key[aa])
                OldName = os.path.join(path,OldDir)
                NewDir = os.rename(OldName,NewName)
        # return NewDir

if __name__=="__main__":
    path = "aa"
    # print(LowerCase(path))
    # print(Capitalize(path))