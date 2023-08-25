# required modules
# from turtle import *
import turtle
import random

w = 500
h = 500
c = 5 # 每邊幾個烏龜
turtle.setup(w, h)  # 調整視窗大小
turtle.colormode(255)

# player_list = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
player_list = [turtle.Turtle() for i in range(c*c) ]

for j in range(c):
    for i in range(c):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        player_list[j*c+i].penup()
        player_list[j*c+i].goto(-w/(2*c)*(c-1) + w/c*i, h/(2*c)*(c-1) - h/c*j)
        player_list[j*c+i].shape('turtle')
        player_list[j*c+i].color(r, g, b)
        player_list[j*c+i].turtlesize(2, 2)

# 旋轉
for a in range(0, 361, 10):
    for i in range(c*c):
        player_list[i].setheading(a)


turtle.done()