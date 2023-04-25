import pygame
from constants import *


# creates the board class
class Board:
    # board object
    def __init__(self, width, height, screen, difficulty, board):
        self.selected_col = 0
        self.selected_row = 0
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = board

    # draws entire board
    def draw(self, screen):

        # draws thick horizontal lines for 9x9 board
        for i in range(1, BOARD_ROWS + 1):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH
            )

        # draws thin horizontal lines within each of the original 9x9 cells
        for i in range(0, INNER_ROWS):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, i * IN_SQUARE_SIZE),
                (WIDTH, i * IN_SQUARE_SIZE),
                IN_LINE_WIDTH
            )

        # draws thick 9x9 board horizontal lines
        for i in range(1, BOARD_COLS):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (i * SQUARE_SIZE, 0),
                (i * SQUARE_SIZE, 675),
                LINE_WIDTH
            )

        # draws thin vertical lines within each of the original 9x9 cells
        for i in range(0, INNER_ROWS + 1):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (i * IN_SQUARE_SIZE, 0),
                (i * IN_SQUARE_SIZE, 675),
                IN_LINE_WIDTH
            )

    def select(self, row, col):
        # handles a selection on the board on the given row and column indices
        self.selected_row = row
        self.selected_col = col

    def click(self, x, y):
        # handles clicking on the board based on the given x and y coordinates
        if x < 0 or x > self.width or y < 0 or y > self.height:
            return

        # Calculates the row and column based on the click coordinates
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE

        # Calls the select method to select the cell
        self.select(row, col)

    def clear(self):
        # This method handles clearing the selected cell on the board
        self.selected_row = None
        self.selected_col = None

    def sketch(self, value):
        # allows sketching a tentative value in the currently selected cell
        if self.selected_row is not None and self.selected_col is not None:
            self.board[self.selected_row][self.selected_col] = value

    def place_number(self, value):
        # allows placing a confirmed value in the currently selected cell
        if self.selected_row is not None and self.selected_col is not None:
            self.board[self.selected_row][self.selected_col] = value

    def reset_to_original(self):
        # resets the board back to its original state
        self.board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

    def is_full(self):
        # checks if the board is completely filled with numbers
        for row in self.board:
            if 0 in row:
                return False
        return True

    def update_board(self):
        # This method updates the visuals of the board to reflect the current state
        # of the board's data
        pass

    def find_empty(self):
        # finds the next empty cell on the board (if any)
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.board[row][col] == 0:
                    return row, col
        return None, None

    def check_board(self, board):
        # Checks if the board is valid according to Sudoku rules

        # Check rows
        valid_row = True
        for row in board:
            for value in row:
                if row.count(value) > 1 or value == 0:
                    valid_row = False

        # Check columns
        valid_col = False
        col = 0
        while col < 8:
            column = [board[row][col] for row in range(BOARD_ROWS)]
            if self.is_valid(column):
                valid_col += 1
                if valid_col == 9:
                    valid_col = True
            col += 1

        # Check 3x3 grids
        valid_grid = 0
        for i in range(0, BOARD_ROWS, 3):
            for j in range(0, BOARD_COLS, 3):
                grid = [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
                if self.is_valid(grid):
                    valid_grid += 1
                    if valid_grid == 9:
                        valid_grid = True

        if valid_row and valid_col and valid_grid:
            return [True, valid_row, valid_col, valid_grid]
        else:
            return False

    def is_valid(self, board):
        # Helper method to check if a list of numbers is valid (no duplicates except for zeros)
        amount = []
        current_run = board[0]
        current_count = 1
        for value in range(1, len(board)):
            if board[value] != 0:
                current_count += 1
            else:
                amount.append(current_count)
                current_run = board[value]
                current_count = 1
        amount.append(current_count)
        return amount

