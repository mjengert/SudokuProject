import pygame, sys
from constants import *
from board import Board
from cell import Cell

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')
screen.fill(BG_COLOR)
game1 = Board(WIDTH, HEIGHT, screen, 'n/a')
game1.draw(screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()