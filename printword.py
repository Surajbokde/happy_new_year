
import turtle
import random
from alphabet import alphabet

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed(0)
window = turtle.Screen()
window.bgcolor("#000000")
myPen.pensize(2)
turtle.pensize(3)
def drawcurve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
turtle.speed(4000)
turtle.color('red','pink')
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
drawcurve()


turtle.left(120)
drawcurve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()


def displayMessage(message, fontSize, color, x, y):
    myPen.color(color)
    message = message.upper()

    for character in message:
        if character in alphabet:
            letter = alphabet[character]
            myPen.penup()
            for dot in letter:
                myPen.goto(x + dot[0] * fontSize, y + dot[1] * fontSize)
                myPen.pendown()

            x += fontSize

        if character == " ":
            x += fontSize
        x += characterSpacing

    # Main Program Starts Here


fontSize = 30
characterSpacing = 5
fontColor = "yellow"

message = "Happy new year"
displayMessage(message, fontSize, fontColor, -230, 200)
displayMessage("from",30,'white',-80,-50)
displayMessage("suraj bokde",30,'white',-180,-100)

turtle.mainloop()
