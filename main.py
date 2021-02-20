import os
os.system('') # to enable ANSI escape codes in CMD
import time
import msvcrt
import random
# backup -> if program should run on linux, change for: https://pypi.org/project/getch/

import display
import snake

anaconda = snake.Snake() # initialize snake class
canvas = display.Display() # initialize display class

status = True
display_note = ""

# -------------------------------------------------------------------------------------------------------------------

canvas.Erase() # clear screen
canvas.DisplayBoard() # display board
canvas.SpawnFood(anaconda.body) # spawn food
canvas.DisplaySnake(anaconda.body, anaconda.removed) # display snake



#Game loop
while(True and status):
    canvas.DisplayScore()
    anaconda.SnakeMove() # move snake for a step

    time.sleep(0.1) # wait a bit, so that we dont move too fast

    canvas.DisplaySnake(anaconda.body, anaconda.removed) # update display
    
    if(canvas.BorderCrossing(anaconda.body) or anaconda.SelfCrossing()):
        status = False

    if msvcrt.kbhit(): # check if input was given, if it was ... change direction
       input_key = msvcrt.getch()
       anaconda.ChangeDirection(input_key.decode('utf-8'))
    
    if(canvas.EatFood(anaconda.body)):
        anaconda.Grow()


canvas.Erase() # clear screen
canvas.DisplayBoard() # display board
print("\033[{};{}HGAME OVER!".format(int(canvas.size/2),canvas.size-2),end="") # display food
print("\033[{};0H".format(canvas.size+5))
canvas.DisplayScore()
    
