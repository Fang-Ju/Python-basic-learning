import turtle as t
import random

def 畫正方形(x,y,size,r,g,b) :
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

t.setup(width=1400, height=600)  # 調整視窗大小
t.speed(speed=0)    #烏龜畫圖速度 1(慢) ~ 10(快)，0(最快)
t.colormode(255)
t.hideturtle()

# #畫指定顏色正方形在四角
# 畫正方形(-650,250,100,0,255,0)
# 畫正方形(650,250,100,255,0,0)
# 畫正方形(-650,-250,100,0,0,255)
# 畫正方形(650,-250,100,255,255,0)

# 畫25個不同顏色的方形陣列
n = 120 # 畫下一個方形中心 與 前一個方形中心 的移動距離
for j in range(4): #列
    for i in range(5): #行
        # r g b 隨機選色
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        x = -650 + i*n # x軸起始座標+移動距離
        y = 250 - j*n # y軸起始座標+移動距離

        畫正方形(x, y, 100, r, g, b)

t.done()