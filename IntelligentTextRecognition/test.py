#coding:utf-8
import os
from PIL import Image
import pytesseract

def readImg(pat):

    # 文件夹下的所有文件列表
    imglist = os.listdir(pat)
    # 遍历列表
    for info in imglist:
        domain = os.path.abspath(pat) # 获取文件夹路径
        info = os.path.join(domain,info) # 将路径名与文件名结合起来，形成一个完整的文件路径
        # info = open(info,'r') #读取文件内容
        Img = Image.open(info)
        text = pytesseract.image_to_string(Img, lang='chi_sim')  # 设置为中文文字的识别
        fo = open('wx.txt', 'a', encoding="utf-8")
        fo.write(text)
        print(text)  #使用readline函数读取每条信息，（使用read可以获取全部信息）
        # info.close()
    fo.close()
    return fo.closed



if __name__ == '__main__':
    # 目标文件夹路径
    # pat = r'C:\Users\朱龙龙\Pictures\花熊'
    # pat = r"C:\Users\朱龙龙\Pictures\Camera Roll"
    # pat = r"C:\Users\朱龙龙\Pictures\QQ"
    # pat = r'C:\Users\朱龙龙\Pictures\新浪微博'
    pat = r"C:\Users\朱龙龙\Pictures\微信"
    readImg(pat)