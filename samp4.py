import turtle
from PIL import Image, ImageTk

# 画像を読み込む
image = ImageTk.PhotoImage(Image.open("./sample.png"))

# turtleを設定する
turtle.setup(image.size[0], image.size[1])
turtle.bgpic("./sample.png")
turtle.shape("turtle")

# turtleを操作する
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# turtleを終了する
turtle.done()
