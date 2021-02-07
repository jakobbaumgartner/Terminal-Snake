import display
import board
import os
os.system('') # to enable ANSI escape codes in CMD
import time
import snake

cobra = snake.Snake
display.erase()
playingboard = board.createboard(60,60)
board.displayboard(playingboard)
# print("\033[15;16f hello")
# print("\033[65;0f hello")
# \033[<L>;<C>H

bitline = 5
bitcollumn = 5
itter = 0

board.displaysnake(cobra.body)

