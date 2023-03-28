import turtle
import random

# 色のリスト
colors = ["#FFC312", "#C4E538", "#12CBC4", "#FDA7DF", "#ED4C67", "#F79F1F", "#A3CB38"]

# 画面の設定
screen = turtle.Screen()
screen.bgcolor("#2C3A47")
screen.setup(600, 600)

# ペンの設定
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.goto(0, 0)
pen.pendown()

# 円を描画するループ
for i in range(20):
    pen.color(random.choice(colors))
    pen.begin_fill()
    pen.circle(random.randint(20, 100))
    pen.end_fill()
    pen.right(random.randint(0, 360))

# 星を描画するループ
for i in range(50):
    pen.penup()
    pen.goto(random.randint(-250, 250), random.randint(-250, 250))
    pen.pendown()
    pen.color(random.choice(colors))
    pen.pensize(random.randint(1, 5))
    pen.begin_fill()
    for j in range(5):
        pen.forward(30)
        pen.right(144)
    pen.end_fill()
    pen.right(random.randint(0, 360))

# 終了処理
turtle.done()
