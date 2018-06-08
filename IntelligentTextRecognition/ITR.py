#coding:utf-8
from PIL import Image
import pytesseract


Img = Image.open(r'C:\PythonProgram\IntelligentTextRecognition\a1.png')
text = pytesseract.image_to_string(Img,lang='chi_sim') # 设置为中文文字的识别
# text = pytesseract.image_to_string(Image.open(r'C:\PythonProgram\IntelligentTextRecognition\a1.png'),lang='eng') # 设置为英文文字的识别

# print(text)

# 打开一个文件
fo = open('aa.txt','w',encoding="utf-8")
fo.write(text)
print(fo)
# 关闭打开的文件
fo.close()