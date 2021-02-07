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
    print(width)

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
            
