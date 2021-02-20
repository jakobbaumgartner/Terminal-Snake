def displaysnake (body):
    # we draw every element of the body on the board

    for rank, element in enumerate(reversed(body)):
        if(rank == 0):
            print("\033[{};{}f%".format(element[0], element[1]))
        else:
            print("\033[{};{}fo".format(element[0], element[1]))
    
    print("\033[65;0f")

