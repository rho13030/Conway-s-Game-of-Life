import pygame
import numpy as np

WIDTH = 1000
HEIGHT = 1000

class Board:
    def __init__(self, surface, width, height, scale, offset):
        """
        Description
        -----------
        constructor for a board instance. 

        Parameters
        ----------
        surface: Surface object. (You can think of this as a 2D array where each element corresponds to a pixel on screen)
            the canvas upon which the game is going to be drawn and played. Refer to main.py to see how it is initialized. 
        width : int
            width of the screen
        height : int
            height of the screen
        scale: int
            the factor by which the canvas is divided into blocks. Used to get the number of columns and rows.
        offset: int
            the gap between each blocks. Refer to draw_grid method to see how it's used

        Return
        ------
        a board instance with information about the basic layout of the canvas
        """
        self.surface = surface
        self.width = width
        self.height = height 
        self.scale = scale
        self.offset = offset

class Conway:
    def __init__(self, board, grid, alive=(147,250,171), dead=(150,116,245)):
        """
        Description
        -----------
        constructor for a Conway game 

        Parameters
        ----------
        board : Board
            instance of a Board. Refer to the Board class
        columns : int
            Number of columns 
        rows : int
            Number of rows
        grid : numpy array object
            A numpy 2D array. Refer to create_grid function in main.py
        alive : tuple
            3-tuple with rgb values for color green
        dead : tuple
            3-tuple with rgb values for color lavendar

        Return
        ------
        an instance of a Conway game
        """
        self.board = board
        self.columns = int(board.height/board.scale)
        self.rows = int(board.width/board.scale)
        self.grid = grid
        self.alive = alive
        self.dead = dead

    def get_neighbors(self, x, y):
        """
        Description
        -----------
        a helper method for getting the number of alive neighbors 

        Parameters
        ----------
        x : int 
            The x-coordinate index of a particular block in the grid
        y : int 
            The y-coordinate index of a particular block in the grid

        Return
        ------
        count : int 
            The number of alive neighbors around a particular block in the grid
        """
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        count = 0
        for dr, dc in neighbors:
            r, c = x + dr, y + dc
            if 0 <= r < self.rows and 0 <= c < self.columns:
                count += self.grid[r][c]
        return count
    
    def update_block(self, x, y):
        """
        Description
        -----------
        a method that updates the status of the block--dead or alive depending on the current state of the block

        Parameters
        ----------
        x : int 
            The x-corrdinate index of a particular block in the grid
        y : int
            The y-coordinate index of a particular block in the grid

        Return
        ------
        an integer--1 for alive and 0 for dead for the next state of the game
        """
        cell_of_interest = self.grid[x,y]
        alive_neighbors = self.get_neighbors(x, y)
    
        if(cell_of_interest == 1):
            if(alive_neighbors<2):
                return 0
            elif(alive_neighbors==2 or alive_neighbors==3):
                return 1
            elif(alive_neighbors>3):
                return 0
        else:
            if(alive_neighbors==3):
                return 1
            else:
                return 0
            
    def run(self):
        """
        Description
        -----------
        Runs the game by calling the draw_grid and update_grid methods.

        This method is responsible for managing the game's main loop, where the current state of the grid
        is drawn and updated based on the game's rules. 

        Return
        ------
        None
        """
        self.draw_grid()
        self.update_grid()
            
    def update_grid(self):
        """
        Description
        -----------
        a method that updates the state of the grid by iterating through each block in the grid and calling the update_block() method. 
        Assigns the updated_grid to the old grid

        Return
        ------
        None
        """
        updated_grid = self.grid.copy()
        for row in range(updated_grid.shape[0]):
            for col in range(updated_grid.shape[1]):
                updated_grid[row, col] = self.update_block(row, col)

        self.grid = updated_grid
    
    def draw_grid(self):
        """
        Description
        -----------
        Draws the current status of the grid and displays it on the user's screen.

        Each block is drawn based on its dimensions and dead/alive status. 
        The grid is represented as a 2D array where 1 indicates a live cell and 0 indicates a dead cell.
    
        The method iterates through each cell in the grid, calculates its position, and draws the appropriate 
        rectangle on the display surface.

        Return
        ------
        None

        Reference
        ---------
         .. [1] Open AI: ChatGpt - https://chat.openai.com/ 
         Referred to the function definition of pygame.draw.Rect to apply it to my code
        """
        for row in range(self.rows):
            for col in range(self.columns):
                cell_x = col * self.board.scale
                cell_y = row * self.board.scale
                cell_rect = pygame.Rect(cell_x, cell_y, self.board.scale - self.board.offset, self.board.scale - self.board.offset)
                if self.grid[row, col] == 1:
                    pygame.draw.rect(self.board.surface, self.alive, cell_rect)
                else:
                    pygame.draw.rect(self.board.surface, self.dead, cell_rect)