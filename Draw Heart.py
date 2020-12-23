import turtle
import time


def hart_arc():
    for i in range(200):
        turtle.right(1)
        turtle.forward(2)


def move_pen_position(x, y):
    turtle.hideturtle()
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.showturtle()


love = input("Please input sentence: ")
signature = input("Please give your name: ")
if love == '':
    love = 'I Love You.'
turtle.setup(width=800, height=500)
turtle.color('red', 'pink')
turtle.pensize(3)
turtle.speed(1)
move_pen_position(x=0, y=-180)
turtle.left(140)
turtle.begin_fill()
turtle.forward(224)
hart_arc()
turtle.left(120)
hart_arc()
turtle.forward(224)
turtle.end_fill()
move_pen_position(0, 0)
turtle.hideturtle()
turtle.color('#CD5C5C', 'pink')
turtle.write(love, font=('Arial', 30, 'bold'), align="center")
if signature != '':
    turtle.color('red', 'pink')
    time.sleep(2)
    move_pen_position(180, -180)
    turtle.hideturtle()
    turtle.write(signature, font=('Arial', 20), align="center")
window = turtle.Screen()
window.exitonclick()