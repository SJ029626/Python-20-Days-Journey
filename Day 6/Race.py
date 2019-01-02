import turtle
from turtle import *
from random import randint

window = turtle.Screen()
window.bgcolor("red")
for step in range(13):
  write(step, align='center')
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

ada = Turtle()
ada.color('pink')
ada.shape('turtle')

ada.penup()
ada.goto(-30, -50)
ada.pendown()

for turn in range(10):
  ada.right(36)

brad = Turtle()
brad.color('blue')
brad.shape('turtle')

brad.penup()
brad.goto(-30, -70)
brad.pendown()

for turn in range(72):
  brad.left(5)

angie = Turtle()
angie.shape('turtle')
angie.color('green')

angie.penup()
angie.goto(-30, -90)
angie.pendown()

for turn in range(60):
  angie.right(6)

jim = Turtle()
jim.shape('turtle')
jim.color('orange')

jim.penup()
jim.goto(-30, -110)
jim.pendown()

for turn in range(30):
  jim.left(12)

brownie = Turtle()
brownie.shape('turtle')
brownie.color('black')

brownie.penup()
brownie.goto(-30, -130)
brownie.pendown()

for turn in range(30):
  brownie.left(12)
for turn in range(100):
  ada.forward(randint(1,5))
  brad.forward(randint(1,5))
  angie.forward(randint(1,5))
  jim.forward(randint(1,5))
  brownie.forward(randint(1,5))
