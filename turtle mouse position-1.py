# #!/usr/bin/python3
# # write tkinter as Tkinter to be Python 2.x compatible
# from tkinter import *
# def hello(event):
#     print("Single Click, Button-l")
# def quit(event):
#     print("Double Click, so let's stop")
#     import sys; sys.exit()  # 把程式強迫中斷
#
# widget = Button(None, text='Mouse Clicks')
# widget.pack()
# widget.bind('<Button-1>', hello)
# # widget.bind('<Button-3>', hello)
# widget.bind('<Double-1>', quit)
# # widget.bind('<Double-Button-1>', quit)
# widget.mainloop()


# ----------------------------
# from tkinter import *
#
# def motion(event):
#   print("Mouse position: (%s %s)" % (event.x, event.y))
#   return
#
# master = Tk()
# whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
# msg = Message(master, text = whatever_you_do)
# msg.config(bg='lightgreen', font=('times', 24, 'italic'))
# msg.bind('<Motion>',motion)
# msg.pack()
# mainloop()

# -------------------------------
# from turtle import *
# import turtle as tur
# import time as t
#
#
# def on_click(i, j):   # 負責跳出迴圈 (while not click) 讓程式繼續畫下一條線
#     global click
#     click = True
#
# def waitforclick():  # 負責更新畫面與等待
#     global click
#     tur.update()
#     click = False
#     while not click:
#         tur.update()
#         t.sleep(.1)
#     click = False
#
#
# click = False
# tur.onscreenclick(on_click)   # 綁定 on_click 函式(優先權最大)， 持續監聽有無按下左鍵，有 : 就立刻執行 on_click 函式
# tur.update()
#
# for _ in range(4):  # 等待到有人按左鍵就畫下一條線，總共畫四條線
#     waitforclick()
#     tur.forward(100)
#     tur.left(90)
#
# tur.exitonclick()  # 當按下左鍵 程式結束跳掉