import os
os.system('') # to enable ANSI escape codes in CMD
import time
import msvcrt
import random
import json
import time
import operator

# backup -> if program should run on linux, change for: https://pypi.org/project/getch/

import display
import snake
import menu


anaconda = snake.Snake() # initialize snake class
canvas = display.Display() # initialize display class
gamemenu = menu.Menu()

game_status = True # while game runs
program_status = True # while program runs

display_note = ""

# -------------------------------------------------------------------------------------------------------------------


while(program_status):
    #Game loop

    if (gamemenu.mode == 0):
        canvas.Erase() # clear screen
        gamemenu.DisplayMenu(canvas.size)
    
        input_key = input()

        if(input_key == '1'):
            gamemenu.mode = 1
            canvas.__init__()
        
        if(input_key == '2'):
            gamemenu.mode = 0
            canvas.size = 8
            canvas.__init__()

        if(input_key == '3'):
            gamemenu.mode = 0
            canvas.size = 16
            canvas.__init__()

        if(input_key == '4'):
            gamemenu.mode = 0
            canvas.size = 32
            canvas.__init__()

       
    
    if (gamemenu.mode == 1):
        
        canvas.Erase() # clear screen
        canvas.DisplayBoard() # display board
        

        canvas.Erase() # clear screen
        canvas.DisplayBoard() # display board

        canvas.SpawnFood(anaconda.body) # spawn food
        canvas.DisplaySnake(anaconda.body, anaconda.removed) # display snake

        while(game_status):

            canvas.DisplayScore()

            anaconda.SnakeMove() # move snake for a step

            time.sleep(0.1) # wait a bit, so that we dont move too fast

            canvas.DisplaySnake(anaconda.body, anaconda.removed) # update display
            
            if(canvas.BorderCrossing(anaconda.body) or anaconda.SelfCrossing()):
                game_status = False

            if msvcrt.kbhit(): # check if input was given, if it was ... change direction
                input_key = msvcrt.getch()
                anaconda.ChangeDirection(input_key.decode('utf-8'))
            
            if(canvas.EatFood(anaconda.body)):
                anaconda.Grow()


        canvas.Erase() # clear screen
        canvas.DisplayBoard() # display board
        print("\033[{};{}HGAME OVER!".format(int(canvas.size/2),canvas.size-2),end="") # display game over
        print("\033[{};0H".format(canvas.size+5)) # move to the bottom of the screen
        canvas.DisplayScore()

        print("\033[{};{}HPress Enter to return to menu.".format(int(canvas.size/2+4),canvas.size-8),end="")  # wait for conformation
        input()
        game_status = True
        gamemenu.mode = 0

      

        anaconda.NewGame() # get ready for a new game
        canvas.NewGame()

    if (gamemenu.mode == 2):
        canvas.Erase() # clear screen
        canvas.ScoreBoard()

        print("\033[{};{}HPress Enter to return to menu.".format(2,canvas.size-8),end="")  # wait for conformation
        input()


    
