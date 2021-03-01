def createGame():
    """Creation of the playing field: the location of mines
       and counting the number of mines around the cells without mines
    """
    pass


def show():
    """The function displays the state of the current
       playing field
    """
    pass


def goPlayer():
    """Function for user input of coordinates
       closed cells of the playing field
    """
    pass


def isFinish():
    """Determining the current state of the game:
       won, lost, the game continues
    """
    pass


def startGame():
    """Game launch function: the playing field is displayed,
       the player opens any closed cell, the result is checked
       for the presence of a mine or a winning situation
    """
    while isFinish():
        show()
        goPlayer()
    return 0


startGame()
print("Game over !")