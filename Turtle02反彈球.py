import turtle

def 畫座標十字線(a) :
    '''
    畫座標十字線
    :param a: 是一個元組 (width,height)
    :return: 沒有回傳
    '''
    turtle.goto(0,0)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(a[0]/2)
    turtle.left(180)
    turtle.forward(a[0])
    turtle.left(180)
    turtle.forward(a[0]/2)
    turtle.left(90)
    turtle.forward(a[1]/2)
    turtle.left(180)
    turtle.forward(a[1])
    turtle.left(180)
    turtle.forward(a[1]/2)
    turtle.left(270)
    turtle.penup()

turtle.setup(1200,800)
turtle.bgcolor('royal blue')
turtle.hideturtle()
turtle.color("white", "white")
turtle.tracer(0)

x = 0
y = 0
xd = 2
yd = 1
while True :

    turtle.clear()  #  螢幕擦乾淨
    畫座標十字線((1200, 800))
    turtle.penup()  #  筆拿起來
    turtle.goto(x,y)  #  走到指定的位置
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()  # 筆拿起來
    turtle.update()

    if not -550 <= x <= 550:
        xd = -xd

    x = x + xd

    if not -400 <= y <= 300:
        yd = -yd

    y = y + yd


turtle.done()