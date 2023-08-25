import turtle
import random
import fangrumodule

# 環境
w = 500
h = 500
c = 3
turtle.setup(w, h)
bgcolor_str = random.sample(fangrumodule.COLORS, 1)
turtle.bgcolor(bgcolor_str[0])

for j in range(c):
    for i in range(c):
        fangrumodule.andriod_icon(1/c, -w/(2*c)*(c-1)+i*w/c,-h/(2*c)*(c-1)+j*h/c, random_2color=True)


turtle.done()
