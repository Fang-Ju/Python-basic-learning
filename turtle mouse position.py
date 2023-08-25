import turtle
def position(event):
    i,j = event.x, event.y
    print('{}, {}'.format(i, j))

ws = turtle.getcanvas()  # 得到一個畫布物件( 是tkinter的畫布canvas物件 )
ws.bind('<Motion>', position)
turtle.done()