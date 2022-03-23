import turtle
import math
import random

wn = turtle.Screen()

wn.bgcolor('black')
Albert = turtle.Turtle()
Albert.speed(20)
Albert.color('white')
rotate = int(360)

def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size = size - 4
def drawSpecial(t,size,repeat):
    for i in range(repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(Albert,100,10)
Steve = turtle.Turtle()
Steve.speed(20)
Steve.color('mediumslateblue')
rotate = 90

drawSpecial(Steve,80,10)
Steve = turtle.Turtle()
Steve.speed(20)
Steve.color('purple')
rotate = 90

drawSpecial(Steve,60,10)


Steve = turtle.Turtle()
Steve.speed(20)
Steve.color('black')
drawSpecial(Steve,50,10)