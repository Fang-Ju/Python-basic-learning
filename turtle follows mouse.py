'''
左鍵拖曳烏龜畫線
'''
# from turtle import *
# from turtle import Turtle, Screen
#
# def drag(i, j):
#     tur.ondrag(None)  # 取消綁定:  先暫停這個功能 不呼叫
#     tur.setheading(tur.towards(i, j))
#     tur.goto(i, j)
#     tur.ondrag(drag)  # 綁定:  再開啟這個功能
#
# ws = Screen()
# tur = Turtle('turtle')
# tur.speed('fastest')
# tur.ondrag(drag)  # 滑鼠左鍵 拖曳
# ws.mainloop()


# -----------------------
'''
左鍵拖曳烏龜畫線
右鍵清除畫面
'''
from turtle import *
import turtle
from turtle import Screen, Turtle

ws = Screen()
tur = turtle.Turtle()
tur.speed(0)
def dragging(x, y):
    tur.ondrag(None)
    tur.setheading(tur.towards(x, y))
    tur.goto(x, y)
    tur.ondrag(dragging)
def clickRight(x, y):
    print(1)
    tur.clear()
def main():
    turtle.listen()  # 傾聽 使用這用此程式實在幹嘛 #聽聽看滑鼠有沒有在動

    tur.ondrag(dragging)
    dragging
    turtle.onscreenclick(clickRight, 3)

    ws.mainloop()


main()