import random

def RandomString(seed):
    # 随机生成8位的字符串
    # seed = "TAGC"
    sa = []
    for i in range(8):
        sa.append(random.choice(seed))
        salt = ''.join(sa)
    return salt

if __name__ == "__main__":
    seed = "TAGC"
    lis = []
    for i in range(10):
        lis.append(RandomString(seed))
        # print(RandString(seed))
    print(lis)