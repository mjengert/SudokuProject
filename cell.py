import pygame


class Cell:

    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self, coords, coordx, coordy):
        smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 45)
        value = smaller_font.render(f'{self.value}', True, (51, 50, 50))
        if self.value == 0:
            pygame.draw.rect(self.screen, (252, 3, 3), [coordx, coordy, 76, 76], 2)
        else:
            self.screen.blit(value, coords)
            pygame.draw.rect(self.screen, (252, 3, 3), [coordx, coordy, 76, 76], 2)