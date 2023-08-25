import turtle as t
import random
import fangru

# ---- 視窗 設定---
w = 700
h = 700
t.setup(w, h)
t.bgcolor('gray80')
t.hideturtle()
#t.tracer(0)
t.speed(0)

for j in range(2) :
    for i in range(1) :
        # fangru.logo(0, 0, 1.5)

        fangru.logo(-700/(3*2)*(3-1) + 700/3*i  , 700/(3*2)*(3-1) - 700/3*j , 0.3)
        # 畫正方形(  -w/(c*2)*(c-1) + w/c*i  , h/(c*2)*(c-1) - h/c*j ,  w/c , r , g , b )

print(fangru.COLORS)

t.done()