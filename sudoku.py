import pygame, sys
from constants import *
from board import Board
from cell import Cell
# We can discuss font choice and background/color scheme together
# Ones in place hold that spot for testing before we decide

# prints the initial menu where user selects difficulty level
def start_menu():
    pygame.display.set_caption('Sudoku')
    big_font = pygame.font.Font('Rajdhani-Bold.ttf', 75)
    med_font = pygame.font.Font('Rajdhani-Bold.ttf', 55)
    welcome_text = big_font.render('Welcome to Sudoku', True, LINE_COLOR)
    gamemode_text = med_font.render('Select Game Mode:', True, LINE_COLOR)
    wel_box = welcome_text.get_rect()
    gmode_box = gamemode_text.get_rect()
    wel_box.center = (337.5, 150)
    gmode_box.center = (337.5, 350)
    screen.blit(welcome_text, wel_box)
    screen.blit(gamemode_text, gmode_box)

# initializes the menu screen
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_im = pygame.image.load("sudokuim.png")
game1 = Board(WIDTH, HEIGHT, screen, 'n/a')
"game1.draw(screen)"


while True:
    screen.blit(background_im, (0,0))
    start_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()