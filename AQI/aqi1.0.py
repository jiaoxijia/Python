"""
作者：zll
日期： 18/4/8
功能：AQI计算
版本：1.0
"""

def cal_linear(iaqi_lo,bp_lo,bp_loi):
    """
    范围缩放
    :return:
    """
    pass


def cal_pm_iaqi(pm_val):
    """
    计算PM2.5的IAQI
    :param pm_val:
    :return:
    """
    if 0<=pm_val<36:
        iaqi = cal_linear(0,50,0,35,pm_val)


def cal_co_iaqi(co_val):
    """
    计算CO的IAQI
    :param co_val:
    :return:
    """
    pass


def cal_aqi(param_list):
    """
    AQI计算
    :param param_list:
    :return:
    """
    pm_val = param_list[0]
    co_val = param_list[1]
    pass

def main():
    """
    主函数
    :return:
    """
    print("请输入以下信息，以空格分割：")
    input_str = input("(1)PM2.5 (2)CO:")
    str_list = input_str.split(" ")
    pm_val = float(str_list[0])
    col_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(col_val)

    #调用AQI测试

if __name__== "__main__":
    main()