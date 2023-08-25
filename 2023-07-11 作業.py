import turtle                                  #  導入 turtle 模組
from turtle import Screen                      #  創建畫布

turtle.speed(0)                                # 設定繪畫速度為最快
ws = Screen()                                  # 賦值給變數ws
pen_down = True                                # 用於追蹤是否按下滑鼠右鍵，當按下右鍵時，將此變數設為 True。

def toggle_pen(x, y):                         #這個函式用於切換提筆狀態，如果 pen_down 為 False，則提筆　pen_down 為 True 則下筆。
    global pen_down
    if pen_down:
        turtle.penup()
        pen_down = False
    else:
        turtle.pendown()
        pen_down = True

def dragging(x, y):                           #處理滑鼠的拖曳將小烏龜移動到指定的座標 ，並根據滑鼠的移動方向旋轉小烏龜。
    turtle.ondrag(None)
    turtle.setheading(turtle.towards(x, y))   # 根據滑鼠的移動方向旋轉小烏龜。
    turtle.goto(x, y)                         # 將小烏龜移動到指定的座標
    turtle.ondrag(dragging)

def clickRight(x, y):                        #清空畫布
    turtle.clear()

def main():                                 # 監聽並將相應的控制綁定到對應的鼠鍵上
    turtle.shape("turtle")                  # 設定形狀為烏龜
    turtle.color("indigo")                  # 設定顏色為藍色
    turtle.pensize(2)                       # 設定筆的大小為2

    turtle.listen()                          # 監聽
    turtle.onscreenclick(dragging,   btn=1)  # 左鍵來畫圖跟到指定位置
    turtle.onscreenclick(clickRight, btn=2)  # 中間清空畫布
    turtle.onscreenclick(toggle_pen, btn=3)  # 右鍵控制筆的狀態
    ws.mainloop()                            # 啟動畫布的主迴圈，使程式可以接收和處理滑鼠控制

main()