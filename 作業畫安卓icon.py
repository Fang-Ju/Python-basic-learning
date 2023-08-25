
import turtle

# 環境
w = 500
h = 500
turtle.setup(w, h)
turtle.colormode(255)
#turtle.tracer(0)
turtle.speed(8)
turtle.hideturtle()

# 共通顏色(不包含眼睛)
turtle.pencolor(154, 205, 50)
turtle.fillcolor(154, 205, 50)

# 畫圖
# 頭
turtle.penup()
turtle.goto(100, 80)
turtle.pendown()

turtle.setheading(90)
turtle.begin_fill()
turtle.circle(100, 180)
turtle.left(90)
turtle.forward(200)
turtle.end_fill()

# 身體
turtle.penup()
turtle.goto(100, 65)
turtle.pendown()
turtle.begin_fill()
turtle.setheading(180)
turtle.forward(200)
turtle.setheading(270)
turtle.forward(180)
turtle.circle(20, 90)
turtle.forward(160)
turtle.circle(20, 90)
turtle.forward(180)
turtle.end_fill()

# 天線
turtle.pensize(5)

turtle.penup()
turtle.goto(60, 150)
turtle.pendown()
turtle.setheading(50)
turtle.forward(40)

turtle.penup()
turtle.goto(-60, 150)
turtle.pendown()
turtle.setheading(130)
turtle.forward(40)

# 四肢
turtle.pensize(35)
# 腳
turtle.penup()
turtle.goto(50, -130)
turtle.pendown()
turtle.setheading(290)
turtle.forward(60)

turtle.penup()
turtle.goto(-50, -130)
turtle.pendown()
turtle.setheading(270)
turtle.forward(60)
# 手
turtle.penup()
turtle.goto(130, 35)
turtle.pendown()
turtle.setheading(50)
turtle.forward(80)

turtle.penup()
turtle.goto(-130, 35)
turtle.pendown()
turtle.setheading(270)
turtle.forward(80)

# 眼睛
turtle.penup()
turtle.goto(36, 120)
turtle.fillcolor(255, 255, 255)
turtle.begin_fill()
turtle.circle(12)
turtle.goto(-60, 120)
turtle.circle(12)
turtle.end_fill()


turtle.done()


