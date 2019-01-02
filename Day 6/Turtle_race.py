import turtle
from random import randint

#window = turtle.Screen()
#window.bgcolor("red")
for step in range(20):
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

#window.exitonclick()
