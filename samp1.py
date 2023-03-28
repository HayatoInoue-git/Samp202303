'''Pythonのturtleをインポート'''
import turtle


'''次に、画面のサイズや座標の設定をします。'''

turtle.setup(width=800, height=600)
turtle.setworldcoordinates(-200, -150, 200, 150)


'''続いて、ZETA DIVISIONのロゴを描くための関数 draw_zeta() を定義します。'''

def draw_zeta():
    turtle.color('#E6443B')  # 赤 (#E6443B)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, -65)
    turtle.color('#FFFFFF')  # 白 (#FFFFFF)
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.pencolor('#E6443B')  # 赤 (#E6443B)
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(-40, 50)
    turtle.pendown()
    turtle.goto(40, 50)


'''この関数では、まず赤い丸を描き、その中に白い丸を描いています。また、斜めの線も引いています。
最後に、上記で定義した draw_zeta() 関数を呼び出してロゴを描きます。'''

draw_zeta()


'''全体のコードは以下のようになります。

python
import turtle

def draw_zeta():
    turtle.color('#E6443B')  # 赤 (#E6443B)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, -65)
    turtle.color('#FFFFFF')  # 白 (#FFFFFF)
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

    turtle.pencolor('#E6443B')  # 赤 (#E6443B)
    turtle.pensize(10)
    turtle.penup()
    turtle.goto(-40, 50)
    turtle.pendown()
    turtle.goto(40, 50)

turtle.setup(width=800, height=600)
turtle.setworldcoordinates(-200, -150, 200, 150)

draw_zeta()

turtle.done()
'''
