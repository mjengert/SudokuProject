import pygame


class Cell:
    board = []

    def __init__(self, value=0, col=0, row=0, screen=None, coords=0, coordx=0, coordy=0):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.coords = coords
        self.coordx = coordx
        self.coordy = coordy
        Cell.board.append(self)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value
        if self.value != 0:
            smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 45)
            num = smaller_font.render(f'{self.value}', True, (128, 128, 128))
            self.screen.blit(num, (self.coordx + 28, self.coordy + 10))
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), [self.coordx + 3, self.coordy + 3, 71, 71])

    def set_value(self, value):  # copied function from above for different font color
        self.value = value
        if self.value != 0:
            smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 45)
            num = smaller_font.render(f'{self.value}', True, (0, 0, 0))  # changed set values to darker color
            self.screen.blit(num, (self.coordx + 28, self.coordy + 10))
        else:
            pygame.draw.rect(self.screen, (255, 255, 255), [self.coordx + 3, self.coordy + 3, 71, 71])

    def draw(self):
        pygame.draw.rect(self.screen, (252, 3, 3), [self.coordx, self.coordy, 76, 76], 2)
