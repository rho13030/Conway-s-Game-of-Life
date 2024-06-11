"""A collection of function for doing my project."""

import numpy as np

WIDTH = 1000
HEIGHT = 1000

def create_grid(randomize=False):
    """
    Description
    -----------
    creates the grid--a 2D array with blocks that have attributes such as dimensions and dead/alive status--depending on the game mode. 
    If the user wants to simulate Conway's game of life with a customized initial state, randomize is False and it returns a zeroed out
    grid. If the user wants a randomized state, then it returns a randamized grid with each cell containing an integer (0 or 1). 

    Parameter
    ---------
    randomize : boolean 
        determines whether the grid should be randomized or zeroed out for user input to customize it.

    Return
    ------
    grid : numpy 2D array
        A grid depending on the value of randomize
    """
    if randomize:
        grid = np.random.choice([0, 1], size=(int(WIDTH/10), int(HEIGHT/10)))
    else:
        grid = np.zeros((int(WIDTH/10), int(HEIGHT/10)), dtype=int)
    return grid

