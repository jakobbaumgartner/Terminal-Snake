import os
os.system('') # to enable ANSI escape codes in CMD
import time
import msvcrt
# backup -> if program should run on linux, change for: https://pypi.org/project/getch/

import display
import snake

anaconda = snake.Snake() # initialize snake class
canvas = display.Display() # initialize display class

input_key = "b'd'"

# -------------------------------------------------------------------------------------------------------------------

canvas.Erase()
canvas.DisplayBoard()

canvas.DisplaySnake(anaconda.body, anaconda.removed)

#Game loop
while(True):
    anaconda.SnakeMove() # move snake for a step
    time.sleep(0.1)
    canvas.DisplaySnake(anaconda.body, anaconda.removed) # update display
    

    if msvcrt.kbhit(): # check if input was given, if it was ... change direction
       input_key = msvcrt.getch()
       anaconda.ChangeDirection(input_key.decode('utf-8'))
    
