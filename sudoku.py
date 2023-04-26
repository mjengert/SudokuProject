import pygame, sys
from constants import *
from board import Board
from cell import Cell
from sudoku_generator import SudokuGenerator, generate_sudoku, print_board


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
def start_button_outlines(color):
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
def med_button(color):
    smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 30)
    button_med = smaller_font.render('Medium', True, BG_COLOR)
    pygame.draw.rect(screen, color, [337.5 - 70, 500, 140, 40])
    screen.blit(button_med, (337.5 - 50, 500))
    pygame.display.update()


# draws hard button
def hard_button(color):
    smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 30)
    button_hard = smaller_font.render('Hard', True, BG_COLOR)
    pygame.draw.rect(screen, color, [337.5 - 70, 580, 140, 40])
    screen.blit(button_hard, (337.5 - 30, 580))
    pygame.display.update()


# draws reset button
def reset_button(color):
    smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 30)
    button_reset = smaller_font.render('Reset', True, BG_COLOR)
    pygame.draw.rect(screen, color, [168.75 - 70, 700, 140, 40])
    screen.blit(button_reset, (168.75 - 35, 700))
    pygame.display.update()


# draws restart button
def restart_button(color, coordx, coordy):
    smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 30)
    button_restart = smaller_font.render('Restart', True, BG_COLOR)
    pygame.draw.rect(screen, color, [coordx, coordy, 140, 40])
    screen.blit(button_restart, (337.5 - 45, 700))
    pygame.display.update()


# draws exit button
def exit_button(color, coordx, coordy):
    smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 30)
    button_exit = smaller_font.render('Exit', True, BG_COLOR)
    pygame.draw.rect(screen, color, [coordx, coordy, 140, 40])
    screen.blit(button_exit, (506.25 - 25, 700))
    pygame.display.update()


# draws rectangle behind in game buttons for border
def game_button_outlines(color):
    pygame.draw.rect(screen, color, [168.75 - 75, 695, 150, 50])
    pygame.draw.rect(screen, color, [337.5 - 75, 695, 150, 50])
    pygame.draw.rect(screen, color, [506.25 - 75, 695, 150, 50])

def board_full(board):
    for row in board:
        if cell.value == 0:
            return False
    return True


# starts program and draws menu and buttons
game_on = True
while game_on:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill((167, 242, 242))
    start_menu()
    start_button_outlines(BORDER_COLOR)
    easy_button(BUTTON_COLOR)
    med_button(BUTTON_COLOR)
    hard_button(BUTTON_COLOR)
    # initializes the menu screen
    menu = True
    while menu:
        # loop looks at all events within game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # checks mouse position and determines if it is clicked
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 267.5 <= mouse_pos[0] <= 337.5 + 70 and 420 <= mouse_pos[1] <= 420 + 40:
                    # creates game board and starts the generator for easy diff.
                    sudoku_gen = generate_sudoku(9, 30)
                    game1 = Board(WIDTH, HEIGHT, screen, 'Easy', sudoku_gen)
                    print_board(sudoku_gen)
                    menu = False
                if 267.5 <= mouse_pos[0] <= 337.5 + 70 and 500 <= mouse_pos[1] <= 500 + 40:
                    # creates game board and starts the generator for medium diff.
                    sudoku_gen = generate_sudoku(9, 40)
                    game1 = Board(WIDTH, HEIGHT, screen, 'Medium', sudoku_gen)
                    print_board(sudoku_gen)
                    menu = False
                if 267.5 <= mouse_pos[0] <= 337.5 + 70 and 580 <= mouse_pos[1] <= 580 + 40:
                    # creates game board and starts the generator for hard diff.
                    sudoku_gen = generate_sudoku(9, 50)
                    game1 = Board(WIDTH, HEIGHT, screen, 'Hard', sudoku_gen)
                    print_board(sudoku_gen)
                    menu = False
            # changes the color of the button if it is being hovered over
            if 267.5 <= mouse_pos[0] <= 337.5 + 70 and 420 <= mouse_pos[1] <= 420 + 40:
                easy_button(HOVER_BUTTON)
            elif 267.5 <= mouse_pos[0] <= 337.5 + 70 and 500 <= mouse_pos[1] <= 500 + 40:
                med_button(HOVER_BUTTON)
            elif 267.5 <= mouse_pos[0] <= 337.5 + 70 and 580 <= mouse_pos[1] <= 580 + 40:
                hard_button(HOVER_BUTTON)
            # if button isn't being hovered over, it returns back to original color
            else:
                easy_button(BUTTON_COLOR)
                med_button(BUTTON_COLOR)
                hard_button(BUTTON_COLOR)
        pygame.display.update()

    # when difficulty is chosen, second while loop begins and sudoku board and buttons is printed
    screen.fill(BG_COLOR)
    game1.draw(screen)
    # list of all cells on game board and uses values from the generated sudoku board
    all_cells = [Cell(sudoku_gen[0][0], 0, 0, screen, (0, 0), 0, 0),
                 Cell(sudoku_gen[0][1], 0, 1, screen, (75, 0), 75, 0),
                 Cell(sudoku_gen[0][2], 0, 2, screen, (150, 0), 150, 0),
                 Cell(sudoku_gen[0][3], 0, 3, screen, (225, 0), 225, 0),
                 Cell(sudoku_gen[0][4], 0, 4, screen, (300, 0), 300, 0),
                 Cell(sudoku_gen[0][5], 0, 5, screen, (375, 0), 375, 0),
                 Cell(sudoku_gen[0][6], 0, 6, screen, (450, 0), 450, 0),
                 Cell(sudoku_gen[0][7], 0, 7, screen, (525, 0), 525, 0),
                 Cell(sudoku_gen[0][8], 0, 8, screen, (600, 0), 600, 0),
                 Cell(sudoku_gen[1][0], 1, 0, screen, (0, 75), 0, 75),
                 Cell(sudoku_gen[1][1], 1, 1, screen, (75, 75), 75, 75),
                 Cell(sudoku_gen[1][2], 1, 2, screen, (150, 75), 150, 75),
                 Cell(sudoku_gen[1][3], 1, 3, screen, (225, 75), 225, 75),
                 Cell(sudoku_gen[1][4], 1, 4, screen, (300, 75), 300, 75),
                 Cell(sudoku_gen[1][5], 1, 5, screen, (375, 75), 375, 75),
                 Cell(sudoku_gen[1][6], 1, 6, screen, (450, 75), 450, 75),
                 Cell(sudoku_gen[1][7], 1, 7, screen, (525, 75), 525, 75),
                 Cell(sudoku_gen[1][8], 1, 8, screen, (600, 75), 600, 75),
                 Cell(sudoku_gen[2][0], 2, 0, screen, (0, 150), 0, 150),
                 Cell(sudoku_gen[2][1], 2, 1, screen, (75, 150), 75, 150),
                 Cell(sudoku_gen[2][2], 2, 2, screen, (150, 150), 150, 150),
                 Cell(sudoku_gen[2][3], 2, 3, screen, (225, 150), 225, 150),
                 Cell(sudoku_gen[2][4], 2, 4, screen, (300, 150), 300, 150),
                 Cell(sudoku_gen[2][5], 2, 5, screen, (375, 150), 375, 150),
                 Cell(sudoku_gen[2][6], 2, 6, screen, (450, 150), 450, 150),
                 Cell(sudoku_gen[2][7], 2, 7, screen, (525, 150), 525, 150),
                 Cell(sudoku_gen[2][8], 2, 8, screen, (600, 150), 600, 150),
                 Cell(sudoku_gen[3][0], 3, 0, screen, (0, 225), 0, 225),
                 Cell(sudoku_gen[3][1], 3, 1, screen, (75, 225), 75, 225),
                 Cell(sudoku_gen[3][2], 3, 2, screen, (150, 225), 150, 225),
                 Cell(sudoku_gen[3][3], 3, 3, screen, (225, 225), 225, 225),
                 Cell(sudoku_gen[3][4], 3, 4, screen, (300, 225), 300, 225),
                 Cell(sudoku_gen[3][5], 3, 5, screen, (375, 225), 375, 225),
                 Cell(sudoku_gen[3][6], 3, 6, screen, (450, 225), 450, 225),
                 Cell(sudoku_gen[3][7], 3, 7, screen, (525, 225), 525, 225),
                 Cell(sudoku_gen[3][8], 3, 8, screen, (600, 225), 600, 225),
                 Cell(sudoku_gen[4][0], 4, 0, screen, (0, 300), 0, 300),
                 Cell(sudoku_gen[4][1], 4, 1, screen, (75, 300), 75, 300),
                 Cell(sudoku_gen[4][2], 4, 2, screen, (150, 300), 150, 300),
                 Cell(sudoku_gen[4][3], 4, 3, screen, (225, 300), 225, 300),
                 Cell(sudoku_gen[4][4], 4, 4, screen, (300, 300), 300, 300),
                 Cell(sudoku_gen[4][5], 4, 5, screen, (375, 300), 375, 300),
                 Cell(sudoku_gen[4][6], 4, 6, screen, (450, 300), 450, 300),
                 Cell(sudoku_gen[4][7], 4, 7, screen, (525, 300), 525, 300),
                 Cell(sudoku_gen[4][8], 4, 8, screen, (600, 300), 600, 300),
                 Cell(sudoku_gen[5][0], 5, 0, screen, (0, 375), 0, 375),
                 Cell(sudoku_gen[5][1], 5, 1, screen, (75, 375), 75, 375),
                 Cell(sudoku_gen[5][2], 5, 2, screen, (150, 375), 150, 375),
                 Cell(sudoku_gen[5][3], 5, 3, screen, (225, 375), 225, 375),
                 Cell(sudoku_gen[5][4], 5, 4, screen, (300, 375), 300, 375),
                 Cell(sudoku_gen[5][5], 5, 5, screen, (375, 375), 375, 375),
                 Cell(sudoku_gen[5][6], 5, 6, screen, (450, 375), 450, 375),
                 Cell(sudoku_gen[5][7], 5, 7, screen, (525, 375), 525, 375),
                 Cell(sudoku_gen[5][8], 5, 8, screen, (600, 375), 600, 375),
                 Cell(sudoku_gen[6][0], 6, 0, screen, (0, 450), 0, 450),
                 Cell(sudoku_gen[6][1], 6, 1, screen, (75, 450), 75, 450),
                 Cell(sudoku_gen[6][2], 6, 2, screen, (150, 450), 150, 450),
                 Cell(sudoku_gen[6][3], 6, 3, screen, (225, 450), 225, 450),
                 Cell(sudoku_gen[6][4], 6, 4, screen, (300, 450), 300, 450),
                 Cell(sudoku_gen[6][5], 6, 5, screen, (375, 450), 375, 450),
                 Cell(sudoku_gen[6][6], 6, 6, screen, (450, 450), 450, 450),
                 Cell(sudoku_gen[6][7], 6, 7, screen, (525, 450), 525, 450),
                 Cell(sudoku_gen[6][8], 6, 8, screen, (600, 450), 600, 450),
                 Cell(sudoku_gen[7][0], 7, 0, screen, (0, 525), 0, 525),
                 Cell(sudoku_gen[7][1], 7, 1, screen, (75, 525), 75, 525),
                 Cell(sudoku_gen[7][2], 7, 2, screen, (150, 525), 150, 525),
                 Cell(sudoku_gen[7][3], 7, 3, screen, (225, 525), 225, 525),
                 Cell(sudoku_gen[7][4], 7, 4, screen, (300, 525), 300, 525),
                 Cell(sudoku_gen[7][5], 7, 5, screen, (375, 525), 375, 525),
                 Cell(sudoku_gen[7][6], 7, 6, screen, (450, 525), 450, 525),
                 Cell(sudoku_gen[7][7], 7, 7, screen, (525, 525), 525, 525),
                 Cell(sudoku_gen[7][8], 7, 8, screen, (600, 525), 600, 525),
                 Cell(sudoku_gen[8][0], 8, 0, screen, (0, 600), 0, 600),
                 Cell(sudoku_gen[8][1], 8, 1, screen, (75, 600), 75, 600),
                 Cell(sudoku_gen[8][2], 8, 2, screen, (150, 600), 150, 600),
                 Cell(sudoku_gen[8][3], 8, 3, screen, (225, 600), 225, 600),
                 Cell(sudoku_gen[8][4], 8, 4, screen, (300, 600), 300, 600),
                 Cell(sudoku_gen[8][5], 8, 5, screen, (375, 600), 375, 600),
                 Cell(sudoku_gen[8][6], 8, 6, screen, (450, 600), 450, 600),
                 Cell(sudoku_gen[8][7], 8, 7, screen, (525, 600), 525, 600),
                 Cell(sudoku_gen[8][8], 8, 8, screen, (600, 600), 600, 600)]

    sudoku_copy_board = sudoku_gen[:]

    for cell in all_cells:
        if cell.value != 0:
            cell.set_cell_value(cell.value)
    # creates copy of original sudoku board cells
    copy_board = []
    for cell in all_cells:
        copy_board.append(cell.value)

    reset_cells = []
    for cell in all_cells:
        if cell.value == 0:
            reset_cells.append(cell)

    # draws buttons for sudoku board screen
    game_button_outlines(BORDER_COLOR)
    exit_button(BUTTON_COLOR, 337.5 - 70, 700)
    restart_button(BUTTON_COLOR, 506.25 - 70, 700)
    reset_button(BUTTON_COLOR)
    # begins game
    game_start = True
    win_screen = False
    lose_screen = False
    while game_start:
        board_complete = board_full(all_cells)
        if board_complete:
            win = game1.check_board(sudoku_copy_board)
            if win:
                win_screen = True
            else:
                lose_screen = True
        for event in pygame.event.get():
            # exits entire game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            mouse_pos = pygame.mouse.get_pos()
            # determines where and if mouse is clicked on each button
            if event.type == pygame.MOUSEBUTTONDOWN:
                # resets all cells to original sudoku board and removes any sketched values
                if 98.75 <= mouse_pos[0] <= 168.75 + 70 and 700 <= mouse_pos[1] <= 700 + 40:
                    for cell in reset_cells:
                        cell.set_sketched_value(0)
                        game1.draw(screen)
                # brings user back to start menu
                if 267.5 <= mouse_pos[0] <= 337.5 + 70 and 700 <= mouse_pos[1] <= 700 + 40:
                    game_start = False
                # allows user to exit the game
                if 436.25 <= mouse_pos[0] <= 506.25 + 70 and 700 <= mouse_pos[1] <= 700 + 40:
                    pygame.quit()
                    sys.exit()
            # changes the color of the button if it is being hovered over
            if 98.75 <= mouse_pos[0] <= 168.75 + 70 and 700 <= mouse_pos[1] <= 700 + 40:
                reset_button(HOVER_BUTTON)
            elif 267.5 <= mouse_pos[0] <= 337.5 + 70 and 700 <= mouse_pos[1] <= 700 + 40:
                restart_button(HOVER_BUTTON, 506.25 - 70, 700)
            elif 436.25 <= mouse_pos[0] <= 506.25 + 70 and 700 <= mouse_pos[1] <= 700 + 40:
                exit_button(HOVER_BUTTON, 337.5 - 70, 700)
            # if button isn't being hovered over, it returns back to original color
            else:
                reset_button(BUTTON_COLOR)
                restart_button(BUTTON_COLOR, 506.25 - 70, 700)
                exit_button(BUTTON_COLOR, 337.5 - 70, 700)
            # draws red box on selected cell for the first col
            if event.type == pygame.MOUSEBUTTONDOWN:
                '''draws red box on the selected cell looks at mouse position (x,y) then draws red box around this 
                coord. re-draws the sudoku board in between each cell selection to allow user to ensure one cell is 
                chosen at a time. calls select() function to record what cell is being selected for input purposes'''
                i, j = -1, -2
                for row in sudoku_copy_board:
                    i += 1
                    j = -2
                    for value in row:
                        j += 1
                        if (75 + 75 * j) <= mouse_pos[0] <= (150 + 75 * j) and (75 * i) <= mouse_pos[1] <= (
                                75 * (i + 1)):
                            game1.draw(screen)
                            for cell in Cell.board:
                                if cell.row == i and cell.col == j + 1:
                                    cell.draw()
                                    game1.select(i, j + 1)
            # looks at all key presses
            if event.type == pygame.KEYDOWN:
                # moves red selection box up
                if event.key == pygame.K_UP:
                    if game1.selected_row != 0:
                        game1.selected_row -= 1
                        game1.draw(screen)
                        for cell in Cell.board:
                            if game1.selected_row == cell.row and game1.selected_col == cell.col:
                                cell.draw()
                # moves red selection box down
                if event.key == pygame.K_DOWN:
                    if game1.selected_row != 8:
                        game1.selected_row += 1
                        game1.draw(screen)
                        for cell in Cell.board:
                            if game1.selected_row == cell.row and game1.selected_col == cell.col:
                                cell.draw()
                # moves red selection box right
                if event.key == pygame.K_RIGHT:
                    if game1.selected_col != 8:
                        game1.selected_col += 1
                        game1.draw(screen)
                        for cell in Cell.board:
                            if game1.selected_row == cell.row and game1.selected_col == cell.col:
                                cell.draw()
                # moves red selection box left
                if event.key == pygame.K_LEFT:
                    if game1.selected_col != 0:
                        game1.selected_col -= 1
                        game1.draw(screen)
                        for cell in Cell.board:
                            if game1.selected_row == cell.row and game1.selected_col == cell.col:
                                cell.draw()
                # the following if statements sketched the corresponding values (1-9) into the selected cell
                if event.key == pygame.K_1:
                    for cell in Cell.board:
                        if game1.selected_row == cell.row and game1.selected_col == cell.col:
                            if cell.value == 0:
                                sudoku_gen[game1.selected_row][game1.selected_col] = 1
                                cell.set_sketched_value(1)
                if event.key == pygame.K_2:
                    for cell in Cell.board:
                        if game1.selected_row == cell.row and game1.selected_col == cell.col:
                            if cell.value == 0:
                                sudoku_gen[game1.selected_row][game1.selected_col] = 2
                                cell.set_sketched_value(2)
                if event.key == pygame.K_3:
                    for cell in Cell.board:
                        if game1.selected_row == cell.row and game1.selected_col == cell.col:
                            if cell.value == 0:
                                sudoku_gen[game1.selected_row][game1.selected_col] = 3
                                cell.set_sketched_value(3)
                if event.key == pygame.K_4:
                    for cell in Cell.board:
                        if game1.selected_row == cell.row and game1.selected_col == cell.col:
                            if cell.value == 0:
                                sudoku_gen[game1.selected_row][game1.selected_col] = 4
                                cell.set_sketched_value(4)
                if event.key == pygame.K_5:
                    for cell in Cell.board:
                        if game1.selected_row == cell.row and game1.selected_col == cell.col:
                            if cell.value == 0:
                                sudoku_gen[game1.selected_row][game1.selected_col] = 5
                                cell.set_sketched_value(5)
                if event.key == pygame.K_6:
                    for cell in Cell.board:
                        if game1.selected_row == cell.row and game1.selected_col == cell.col:
                            if cell.value == 0:
                                sudoku_gen[game1.selected_row][game1.selected_col] = 6
                                cell.set_sketched_value(6)
                if event.key == pygame.K_7:
                    for cell in Cell.board:
                        if game1.selected_row == cell.row and game1.selected_col == cell.col:
                            if cell.value == 0:
                                sudoku_gen[game1.selected_row][game1.selected_col] = 7
                                cell.set_sketched_value(7)
                if event.key == pygame.K_8:
                    for cell in Cell.board:
                        if game1.selected_row == cell.row and game1.selected_col == cell.col:
                            if cell.value == 0:
                                sudoku_gen[game1.selected_row][game1.selected_col] = 8
                                cell.set_sketched_value(8)
                if event.key == pygame.K_9:
                    for cell in Cell.board:
                        if game1.selected_row == cell.row and game1.selected_col == cell.col:
                            if cell.value == 0:
                                sudoku_gen[game1.selected_row][game1.selected_col] = 9
                                cell.set_sketched_value(9)
                # allows for deletion of a sketched values only
                if event.key == pygame.K_BACKSPACE:
                    pos = 0
                    for cell in Cell.board:
                        if game1.selected_row == cell.row and game1.selected_col == cell.col:
                            cell.set_cell_value(copy_board[pos])
                            sudoku_gen[game1.selected_row][game1.selected_col] = 0
                        pos += 1
                # allows for removal of red box once enter is pressed
                if event.key == pygame.K_KP_ENTER:
                    for cell in Cell.board:
                        if game1.selected_row == cell.row and game1.selected_col == cell.col:
                            game1.place_number(cell.value)
                            game1.draw(screen)
        pygame.display.update()

        while win_screen == True:
            screen.fill((167, 242, 242))
            exit_button()
            pygame.display.update()

        while lose_screen == True:
            screen.fill((167, 242, 242))
            pygame.display.update()
