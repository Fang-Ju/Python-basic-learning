from PIL import Image
import numpy as np

with Image.open(r"imgs\2023-3-31.png") as im:  # 模組裡專門開影像的open   # im(隨意命名) 為 Image物件
    im.rotate(0).show()   # Image物件 的 show()  --> 電腦內建用什麼方式展現影像 他就用那個方式show圖
    print(im)   # print 看不到內容 --> <PIL.PngImagePlugin.PngImageFile image mode=RGB size=803x696 at 0x25A6345A6E0>

# image to numpy.array
img = np.array(im)
print(img)
print(type(img))   # <class 'numpy.ndarray'>

# numpy to list
img_list = img.tolist()
print(img_list)
print(type(img_list))  # <class 'list'>