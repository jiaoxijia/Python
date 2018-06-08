


"""
    密码强度验证demo
    作者：zll
    时间:2017/12/04
    V1.0
"""

def main():
    pwd = input("请输入密码：")
    cs = 0
    if pwd.length < 8:
        return
        print("密码长度最少为8位")
    else:
        cs +=1
    if cs <3:
        return
        print("您输入的密码过于简单，请从新设置密码：")
if __name__ =="__main__":
    main()