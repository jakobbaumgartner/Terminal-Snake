import os
os.system('') # to enable ANSI escape codes in CMD
import time
import msvcrt
# backup -> if program should run on linux, change for: https://pypi.org/project/getch/

import display
import snake

anaconda = snake.Snake() # initialize snake class
canvas = display.Display() # initialize display class

# -------------------------------------------------------------------------------------------------------------------

canvas.Erase()
canvas.DisplayBoard()

canvas.DisplaySnake(anaconda.body, anaconda.removed)

anaconda.SnakeMove()
canvas.DisplaySnake(anaconda.body, anaconda.removed)

anaconda.SnakeMove()
canvas.DisplaySnake(anaconda.body, anaconda.removed)

anaconda.SnakeMove()
canvas.DisplaySnake(anaconda.body, anaconda.removed)

anaconda.SnakeMove()
canvas.DisplaySnake(anaconda.body, anaconda.removed)

anaconda.SnakeMove()
canvas.DisplaySnake(anaconda.body, anaconda.removed)


# while(True):
    
#     # time.sleep(1)

#     anaconda.SnakeMove()
#     canvas.DisplaySnake(anaconda.body)
  
     
    # anaconda.direction = msvcrt.getch()
