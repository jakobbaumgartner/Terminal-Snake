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

canvas.Erase()
canvas.DisplayBoard()

canvas.DisplaySnake(anaconda.body, anaconda.removed)

#Game loop
while(True and status):
    anaconda.SnakeMove() # move snake for a step

    time.sleep(0.1) # wait a bit, so that we dont move too fast

    canvas.DisplaySnake(anaconda.body, anaconda.removed) # update display
    
    if(canvas.BorderCrossing(anaconda.body)):
        status = False

    if msvcrt.kbhit(): # check if input was given, if it was ... change direction
       input_key = msvcrt.getch()
       anaconda.ChangeDirection(input_key.decode('utf-8'))
    
    if(canvas.EatFood(anaconda.body)):
        anaconda.Grow()

    
