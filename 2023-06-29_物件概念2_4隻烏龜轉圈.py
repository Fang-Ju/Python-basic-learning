# required modules
# from turtle import *
import turtle
import random

player_list = [turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()]
turtle.colormode(255)

for i in range(4):
    player_list[i].penup()

    player_list[i].shape('turtle')

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    player_list[i].color(r, g, b)

    player_list[i].turtlesize(3, 3)

# 位置
count_ = 0
for y in range(2):
    for x in range(2):
        player_list[count_].goto(-160 + x*320, 160 - y*320)
        count_ += 1

# 旋轉
for a in range(360):
    for i in range(4):
        player_list[i].setheading(a)


turtle.done()