"""Script to run some part of my project."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
from my_module.functions import *
from my_module.classes import *

###
###

# PYTHON SCRIPT HERE
import pygame
import numpy as np

WIDTH = 1000
HEIGHT = 1000

pygame.init() 
pygame.display.set_caption("cogs18 project: Conway's Game of Life") 

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    """
    Description
    -----------
    The main function. This is the main lobby of the program in which everything comes together. Variables and objects are initialized first 
    before executing the main loop. There are two options to this game: (1) randomized board and (2) customized board. If key #2 on the 
    keyboard is pressed,(2) executes and if key #1 is pressed, (1) is executed. There are three modes to this game: menu, draw, and game. 
    The menu mode is the starting page where the user can select the option. The draw mode is specifically for creating a customized board. 
    Upon entering, it shows a blank canvas of grid layout and the user can press each cell/block to change the status. When the user is 
    done, pressing the enter button will change the mode to game, during which the game runs. Honestly I think it's better to draw a state 
    transition diagram for this, but it is what it is. Oh, and the game ends when the user clicks the exit button on the window.

    Reference
    ---------
     .. [1] Open AI: ChatGpt - https://chat.openai.com/ 
     Learned the basics of Pygame, such as initializing pygame modules using pygame.init(), instantiating a Screen object, managing time using the Clock object, etc.
    """
    clock = pygame.time.Clock()
    fps = 60
    mode = 'menu'
    grid = create_grid() #initialize the grid here to avoid UnboundLocalError
    new_board = Board(screen, WIDTH, HEIGHT, scale=10, offset=1)
    conway = Conway(new_board, grid)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if mode == 'menu':
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        mode = 'draw'
                        grid = create_grid()
                        conway = Conway(new_board, grid)  
                    elif event.key == pygame.K_2:
                        mode = 'game'
                        grid = create_grid(randomize=True)
                        conway = Conway(new_board, grid)
            
            elif mode == 'draw':
                cell_size = WIDTH // int(WIDTH // new_board.scale)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    col, row = x // cell_size, y // cell_size
                    grid[row, col] = 1 if grid[row, col] == 0 else 0   

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        mode = 'game'

        screen.fill((0, 0, 0))

        if mode == 'game':
            conway.run()
        elif mode == 'draw':
            conway.draw_grid()

        pygame.display.update()
        clock.tick(fps)

if __name__ == "__main__":
    main()
