import turtle


def draw_square(obj):
    obj.begin_fill()
    for side in range(4):
        obj.forward(20)
        obj.right(90)
    obj.end_fill()
    return None


def main():
    screen = turtle.Screen()
    screen.setup(500, 500)
    screen.tracer(0)  # tell screen to not show automatically
    don = turtle.Turtle()
    don.speed(0)
    don.width(3)
    don.hideturtle()  # hide don, we only want to see the drawing

    don.penup()
    don.goto(-240, 240)
    don.pendown()

    state = 1  # 往右   2 往下   3 往左    4 往上
    speed = 0.1  # 定速0.1

    while True:
        don.clear()
        draw_square(don)
        screen.update()  # only now show the screen, as one of the frames
        don.forward(speed)
        if state == 1:
            if don.xcor() > 215:
                don.forward(20)
                don.right(90)
                state = 2
        elif state == 2:
            if don.ycor() < -215:
                don.forward(20)
                don.right(90)
                state = 3
        elif state == 3:
            if don.xcor() < -220:
                don.forward(20)
                don.right(90)
                state = 4
        else:
            if don.ycor() > 215:
                don.forward(20)
                don.right(90)
                state = 1


if (__name__ == '__main__'):
    main()