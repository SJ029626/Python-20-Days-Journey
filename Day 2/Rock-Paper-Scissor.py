#!/bin/python
from random import randint

print("Player Vs Machine Game")

player=input("Choose Rock(r or R), Paper(p or P), Scissor(s or S):")

print("<------------------------------------->")
print("Symbol Denotion")
print("Rock=> |@|")
print("Paper=>/_/")
print("Scissor=>8<")
print("<-------------------------------------->")

print("***********************************************")
print("Game Begins")
if (player == 'r' or player == 'R'):
  print('|@|', end=' ')
  
elif (player == 'p'or player == 'P') :
  print('/_/', end=' ')
  
elif (player == 's'or player == 'S'):
  print('8<', end=' ')
else:
    print("Invalid Input (!)")
print("VS",end=' ')
machine_choice=randint(1,3)

if (machine_choice == 1) :
  machine = 'r'
  computer='R'
  print('|@|')
  
elif (machine_choice == 2) :
  machine = 'p'
  computer='P'
  print('/_/')
  
else:
    machine = 's'
    computer='S'
    print('8<')
if (player == machine or player== computer):
  print('DRAW!')
  
elif ((player == 'r' or player=='R')and machine == 's'):
  print('Player wins!')
  
elif ((player == 'r' or player=='R')and machine == 'p'):
  print('Machine wins!')
  
elif ((player == 'p' or player=='P')and machine == 'r'):
  print('Player wins!')
  
elif ((player == 'p' or player=='P')and machine == 's'):
  print('Machine wins!')

elif ((player == 's' or player=='S')and machine == 'p'):
  print('Player wins!')
  
elif ((player == 's'or player=='S')and machine == 'r'):
  print('Machine wins!')

print("Game Ends")
print("<===================================================>")