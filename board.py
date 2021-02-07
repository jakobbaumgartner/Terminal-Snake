def createboard(x, y):
    board = []
    row = []
    
    for elementx in range(x):
        row.append("  ")
    for elementy in range(y):
        board.append(row)
    
    return board 

def displayboard(board): 
    height = len(board)
    width = len(board[0])
    # print(width)

    # display board with border:
    print("")
    print("  ",end="")
    for elementx in range(width+1):
        print("##",end="")
    print("")
    for elementy in range(height):
        print("  #", end="")
        
        for elementx in range(width):
         
            print(board[elementy][elementx], end="")
            if elementx == width-1:
                print("#",end="")
        print("")
    print("  ",end="")
    for elementx in range(width+1):
        print("##",end="")

def displaysnake (body):
    # we draw every element of the body on the board

    for rank, element in enumerate(reversed(body)):
        if(rank == 0):
            print("\033[{};{}f%".format(element[0], element[1]))
        else:
            print("\033[{};{}fo".format(element[0], element[1]))
    
    print("\033[65;0f")
