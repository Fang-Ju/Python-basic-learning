# ---------1----------
# from turtle import *
# import turtle
#
#
# def func(i, j):
#     turtle.right(90)
#     turtle.forward(150)
#
#
# turtle.speed(6)
# turtle.forward(100)
# turtle.onclick(func)   # 一定要點到烏龜才有作用
# turtle.done()


# ---------2----------
from turtle import *
import turtle
ws = turtle.Screen()

def func(x, y):
    turtle.goto(x, y)
    turtle.write(str(x) + "," + str(y))

ws.onclick(func)  # 點到視窗任何定方都有作用
ws.mainloop()

