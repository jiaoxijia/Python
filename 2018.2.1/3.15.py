#coding:utf-8
def func(a ,b=5, c=10):
    print 'a is ',a, 'and b is ', b, 'and c is ',c

def say(message,times=1):
    print message * times
def total(a=5,*numbers,**phonebook):
    print "a",a

    #遍历元组中的所有数组
    for single_item in numbers:
        print "single_item",single_item

    #遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print first_part,second_part
#print total(10,1,2,3,Jack=1123,John=2231,Inge=1560)

def print_max(x,y):
    '''Prints the maximum of two numbers.打印两个数字中的最大值
        The two values must be integers.
    '''
    x = int(x)
    y = int(y)

    if x > y:
        return x
    if y >x:
        return y
    else:
        print '''请输入汉字'''


#print print_max(6, 5)
print print_max.__doc__
# if __name__ == "__main__":
#     # func(20,29,1000)
#     # say("hello")
#     # say("world",5)