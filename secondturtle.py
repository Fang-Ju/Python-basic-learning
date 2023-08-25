import turtle

#移動到外圈 長寬400
turtle.penup()
turtle.forward(200)
turtle.left(90)
turtle.pendown()

#畫外框
turtle.forward(200)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(400)
turtle.left(90)
turtle.forward(200)

#移動到內圈 長寬200
turtle.penup()
turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.pendown()

#畫內框
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(200)
turtle.left(90)
turtle.forward(100)



turtle.done()