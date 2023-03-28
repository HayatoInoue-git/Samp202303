import turtle

# 背景を黒色に設定
turtle.bgcolor("black")

# ペンを設定
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(4)

# 外側の円を描画
pen.color("red")
pen.penup()
pen.goto(0, -150)
pen.pendown()
pen.circle(150)

# 内側の円を描画
pen.color("white")
pen.penup()
pen.goto(0, -110)
pen.pendown()
pen.circle(110)

# 中央のZを描画
pen.color("red")
pen.penup()
pen.goto(0, -20)
pen.pendown()
pen.right(60)
pen.forward(70)
pen.right(120)
pen.forward(140)
pen.right(120)
pen.forward(70)

# テキストを描画
pen.color("white")
pen.penup()
pen.goto(0, 80)
pen.write("ZETA DIVISION", align="center", font=("Arial", 24, "normal"))

turtle.done()
