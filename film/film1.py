'''

分形树的绘制
版本：V1.0
日期：17/11/30

'''
import turtle

def draw_branch(brabch_length):
    """
    绘制分形树
    """
    if brabch_length > 5:
        #绘制右侧树枝
        turtle.forward(brabch_length)
        print('向前',brabch_length)
        turtle.right(20)
        print('右转 20')
        draw_branch(brabch_length - 15)

        #绘制左侧树枝
        turtle.left(40)
        print('左转 40')
        draw_branch(brabch_length - 15)

        #返回之前的树枝
        turtle.right(20)
        print('右转20')
        turtle.backward(brabch_length)

def main():
    """主函数"""
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.color('brown')
    draw_branch(80)
    turtle.exitonclick()

if __name__ == '__main__':
    main()

