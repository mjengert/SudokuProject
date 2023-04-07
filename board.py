import pygame
from constants import *


class Board:

    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.diff = difficulty

    # draws entire board
    def draw(self, screen):
        # draws thick horizontal lines for 9x9 board
        for i in range(1, BOARD_ROWS+1):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH
            )

        # draws thin horizontal lines within each of the original 9x9 cells
        for i in range(1, INNER_ROWS):
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
        for i in range(1, INNER_ROWS):
            pygame.draw.line(
                screen,
                LINE_COLOR,
                (i * IN_SQUARE_SIZE, 0),
                (i * IN_SQUARE_SIZE, 675),
                IN_LINE_WIDTH
            )

    def select(self, row, col):
        pass

    def click(self, x, y):
        pass

    def clear(self):
        pass

    def sketch(self, value):
        pass

    def place_number(self, value):
        pass

    def reset_to_original(self):
        pass

    def is_full(self):
        pass

    def update_board(self):
        pass

    def find_empty(self):
        pass

    def check_board(self):
        pass
