import turtle as t
import random

def 畫正方形(x=0, y=0, size=100, r=0, g=0, b=0) :
    # 指定顏色
    t.pencolor(r, g, b)
    t.fillcolor(r, g, b)

    # x,y 在方形的中間
    t.penup()
    t.goto(x,y)
    t.setheading(0)

    # 去左下角頭朝上
    t.fd(size/2)
    t.lt(90)
    t.bk(size/2)

    t.down()
    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()

    return None

w = 600 #視窗寬
h = 600 #視窗高
c = 5 #畫的個數

t.setup(w,h)  # 調整視窗大小
t.speed(speed=0)    #烏龜畫圖速度 1(慢) ~ 10(快)，0(最快)
t.colormode(255)
t.hideturtle()
t.tracer(0) #不追蹤

for j in range(c):
    for i in range(c):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        畫正方形(-w/(c*2)*(c-1) + w/c*i, h/(c*2)*(c-1) - h/c*j, w/c,r,g,b)


t.done()