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


# canvas.erase()
# canvas.displayboard() 

print(anaconda.body)
anaconda.SnakeMove()
print(anaconda.body)




# while(True):
    
#     time.sleep(1)

  

   

#     print("\033[{};{}f%".format(10, 0))
     
#     # anaconda.direction = msvcrt.getch()
