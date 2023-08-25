import turtle as t
import time
# t=turtle
# print(type(t))

def 畫正方形(size) :

    t.begin_fill()
    for i in range(4):
        t.fd(size)
        t.lt(90)
    t.end_fill()

    return None



t.colormode(255)
t.hideturtle()
t.tracer(0)
t.speed(speed=0)

count=5  # 畫方形的數量限制
size=50  # 方的大小
space=5  # 間隔

van = 0 # 現在畫到第幾個
n = 0 # 移動距離(起始位置到現在位置的距離)

r = 255
g = 0
b = 0
t.fillcolor(r, g, b)

while van<count:
    # t.clear()
    t.penup()
    t.goto(-200+n,0)
    t.setheading(270)

    # 寫成自訂函式
    畫正方形(size)

    # 畫正方形
    # t.begin_fill()
    # for i in range(4):
    #     t.fd(size)
    #     t.lt(90)
    # t.end_fill()

    n += (count+size)
    van+=1
    t.update()
    # 暫停 1 秒
    time.sleep(1)

t.done()