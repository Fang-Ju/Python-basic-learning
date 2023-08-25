for i in [100,200,300] :
    print(i)

for i in range(10,20,2) :
    print(i)


import turtle
import random

turtle.colormode(255)

n = 10
for i in range(n):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    turtle.pencolor(r,g,b)
    turtle.fillcolor(r,g,b)

    #移動到外圈 長寬400
    turtle.penup()
    turtle.forward(200/n*(n+1-i))
    turtle.left(90)
    turtle.pendown()


    turtle.begin_fill() #開始填色
    #畫外框
    turtle.forward(200/n*(n+1-i))
    turtle.left(90)
    turtle.forward(400/n*(n+1-i))
    turtle.left(90)
    turtle.forward(400/n*(n+1-i))
    turtle.left(90)
    turtle.forward(400/n*(n+1-i))
    turtle.left(90)
    turtle.forward(200/n*(n+1-i))

    turtle.end_fill()  #封閉圖形結束顏色

    #回原點
    turtle.penup()
    turtle.right(90)
    turtle.backward(200/n*(n+1-i))

##########################

# #移動到內圈 長寬200
# turtle.penup()
# turtle.forward(100)
# turtle.left(90)
# turtle.pendown()
#
# #畫內框
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(200)
# turtle.left(90)
# turtle.forward(200)
# turtle.left(90)
# turtle.forward(200)
# turtle.left(90)
# turtle.forward(100)



turtle.done()