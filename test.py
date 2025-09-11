import turtle
from turtle import *
t = Turtle()
def square(length):
    for i in range(4):
        t.left(90)
        t.forward(length)

# BIGSquare makes a spiral using (amount) of squares, starting from (length) and increasing by the original length given.
# Example: BIGSquare(60, 5) would make a spiral of 60 squares, starting from a length of 5 and increasing by 5 for every square done.
def BIGSquare(amount, length):
    oglength = length
    print("Making a spiral of squares :D")
    for i in range(amount):
        t.speed(0)
        square(length)
        t.left(5)
        length = length + oglength


def star(length):
    for i in range(5):
        t.forward(length)
        t.left(144)

# Works pretty much the same as BIGSquare, but draws stars rather than squares
def BIGStar(amount, length):
    oglength = length
    for i in range(amount):
        t.speed(0)
        star(length)
        t.left(5)
        length = length + oglength
BIGStar(60,10)