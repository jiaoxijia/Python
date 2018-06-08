"""
    功能：52周存钱挑战
    日期： 17/11/30
    V 1.0
"""
def main():
    """
    这个是主函数哦~
    :return:
    """
    money_per_week = 10 #每周存入金额
    i = 1 #创建一个内存空间记录周数
    increase_money = 10 #递增的金额数
    total_week = 52 #总计周数
    saving = 0  #账户累计金额

    while i <= total_week:
        #进行存钱操作
        #saving = saving + money_per_week
        saving = saving + money_per_week
        i += 1
        print('当前是第'+str(i)+"周"+","+"当前金额是："+ str(saving))

if __name__ == '__main__':
    main()