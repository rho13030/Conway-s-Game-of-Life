"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import *
from classes import *

import numpy as np
##
##

def test_create_grid():
    testBoard1 = np.zeros((100,100))
    testBoard2 = create_grid()
    testBoard3 = create_grid(True)

    assert np.size(testBoard1) == np.size(testBoard2)
    assert np.size(testBoard1) == np.size(testBoard3)

def test_get_neighbors():
    #for simplification, I'm testing on a screen that is a 3x3 2D array. Note, however, that 
    #testing on a single cell/block is sufficient to say that this method works for any 2D arrays
    testarr = [[1,0,1],
               [1,1,1],
               [0,0,1]
              ]
    test_board = Board(testarr,600,600,200,10)
    test_conway = Conway(test_board, testarr)
    assert type(test_conway.get_neighbors(1,1)) == int
    assert test_conway.get_neighbors(1,1) == 5

def test_update_block():
    #note that I'm using a numpy array for type-matching
    testarr = np.array([[1,0,1],[1,1,1],[0,0,1]])
    test_board = Board(testarr,600,600,200,10)
    test_conway = Conway(test_board, testarr)
    test_conway.grid[1,1] = test_conway.update_block(1,1)
    assert test_conway.grid[1,1] == 0

def test_update_grid():
    #note that I'm using a numpy array for type-matching
    testarr = np.array([[1,0,1],[1,1,1],[0,0,1]])
    test_board = Board(testarr,600,600,200,10)
    test_conway = Conway(test_board, testarr)
    test_conway.update_grid()
    assert test_conway.grid[1,1] == 0
    



                 
    