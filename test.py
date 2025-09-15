import turtle
from turtle import *
t = Turtle()

# makes a square with each side's length being (length)
def square(length):
    print(f"Creating a square with a side length of {length}")
    for i in range(4):
        t.left(90)
        t.forward(length)

# Makes a rectangle with (l) length and (w) width
def rectangle(l, w):
    print(f"Creating rectangle with {l} length and {w} width")
    for i in range(2):
        t.forward(l)
        t.left(90)
        t.forward(w)
        t.left(90)
rectangle(125,100)




# BIGSquare makes a spiral using (amount) of squares, starting from (length) and increasing by the original length given.
# Example: BIGSquare(60, 5) would make a spiral of 60 squares, starting from a length of 5 and increasing by 5 for every square done.
def BIGSquare(amount, length):
    oglength = length
    print(f"Making a spiral of {amount} squares, with the starting length being {oglength} ")
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
