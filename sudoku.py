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


# prints rectangles behind buttons to create border
def button_outlines(color):
    pygame.draw.rect(screen, color, [337.5 - 75, 415, 150, 50])
    pygame.draw.rect(screen, color, [337.5 - 75, 495, 150, 50])
    pygame.draw.rect(screen, color, [337.5 - 75, 575, 150, 50])


# draws easy button
def easy_button(color):
    smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 30)
    button_easy = smaller_font.render('Easy', True, BG_COLOR)
    pygame.draw.rect(screen, color, [337.5 - 70, 420, 140, 40])
    screen.blit(button_easy, (337.5 - 30, 420))
    pygame.display.update()


# draws medium button
def hard_button(color):
    smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 30)
    button_hard = smaller_font.render('Hard', True, BG_COLOR)
    pygame.draw.rect(screen, color, [337.5 - 70, 580, 140, 40])
    screen.blit(button_hard, (337.5 - 30, 580))
    pygame.display.update()


# draws hard button
def med_button(color):
    smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 30)
    button_med = smaller_font.render('Medium', True, BG_COLOR)
    pygame.draw.rect(screen, color, [337.5 - 70, 500, 140, 40])
    screen.blit(button_med, (337.5 - 50, 500))
    pygame.display.update()


# initializes the menu screen and draws difficulty buttons
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# can change background; placeholder
background_im = pygame.image.load("sudokuim.png")
game1 = Board(WIDTH, HEIGHT, screen, 'n/a')
screen.blit(background_im, (0, 0))
start_menu()
button_outlines((64, 94, 0))
easy_button((51, 50, 50))
med_button((51, 50, 50))
hard_button((51, 50, 50))
"game1.draw(screen)"

while True:
    # loop looks at all events within game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # checks mouse position and determines if it is clicked
        # currently only exits the game for test purposes; will provide functionality after
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 267.5 <= mouse_pos[0] <= 337.5 + 70 and 420 <= mouse_pos[1] <= 420 + 40:
                pygame.quit()
                sys.exit()
            if 267.5 <= mouse_pos[0] <= 337.5 + 70 and 500 <= mouse_pos[1] <= 500 + 40:
                pygame.quit()
                sys.exit()
            if 267.5 <= mouse_pos[0] <= 337.5 + 70 and 580 <= mouse_pos[1] <= 580 + 40:
                pygame.quit()
                sys.exit()
        # changes the color of the button if it is being hovered over
        if 267.5 <= mouse_pos[0] <= 337.5 + 70 and 420 <= mouse_pos[1] <= 420 + 40:
            easy_button((130, 127, 127))
        elif 267.5 <= mouse_pos[0] <= 337.5 + 70 and 500 <= mouse_pos[1] <= 500 + 40:
            med_button((130, 127, 127))
        elif 267.5 <= mouse_pos[0] <= 337.5 + 70 and 580 <= mouse_pos[1] <= 580 + 40:
            hard_button((130, 127, 127))
        # if button isn't being hovered over, it returns back to original color
        else:
            easy_button((51, 50, 50))
            med_button((51, 50, 50))
            hard_button((51, 50, 50))
    pygame.display.update()
