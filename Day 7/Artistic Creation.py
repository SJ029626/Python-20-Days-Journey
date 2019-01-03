#!/bin/python3

from turtle import *
from time import *

# introduce dictionaries
# use a colour picker to find and choose new colours
colours = { 
  'space': '#060608', 
  'moongrey': '#BCBDEF', 
  'verylime': '#A7E30E', 
  'deepsea': '#226363', 
  'reallyraspberry': '#FA057F', 
  'gloomygrey': '#363332', 
  'awesomeorange':  '#F37C06', 
  'coolcyan': '#4FEEF6',
  'perfectpurple': '#6820B0',
  'lovelylemon': '#FBF312',
}

screen = Screen()
screen.setup(400, 400)
screen.bgcolor(colours['space'])

penup()
goto(0, 100)
color(colours['reallyraspberry'])
style = ('Arial', 40, 'bold')
write('Hi', font=style, align='center')
right(90)
forward(60)
color(colours['awesomeorange'])
write('Universe', font=style, align='center')
hideturtle()

sleep(3)

goto(0,0)
color(colours['moongrey'])
dot(350)

setheading(-90)
penup()
hideturtle()
goto(0, 135)
color(colours['verylime'])
style=('Verdana', 20, 'bold')
write('Whale', font=style, align='center')
forward(40)
color(colours['reallyraspberry'])
write('have', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['deepsea'])
write('more', font=('Verdana', 18, 'bold'), align='center')
forward(40)
color(colours['awesomeorange'])
write('Supersonic power', font=('Verdana', 25, 'bold'), align='center')
forward(40)
color(colours['perfectpurple'])
write('than', font=style, align='center')
forward(40)
color(colours['coolcyan'])
write('An', font=('Verdana', 25, 'bold'), align='center')
color(colours['lovelylemon'])
forward(40)
write('Avergae', font=style, align='center')
color(colours['gloomygrey'])
forward(40)
write('human', font=('Verdana', 25, 'bold'), align='center')
color('white')
forward(50)
write('- SJ,-2019', font=('Arial', 14, 'normal'))
