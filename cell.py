import pygame


class Cell:

    def __init__(self, value=0, row=0, col=0, screen=None, coords=0, coordx=0, coordy=0):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.coords = coords
        self.coordx = coordx
        self.coordy = coordy

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        smaller_font = pygame.font.Font('Rajdhani-Bold.ttf', 45)
        num = smaller_font.render(f'{self.value}', True, (51, 50, 50))
        if self.value == 0:
            pygame.draw.rect(self.screen, (255, 255, 255), [self.coordx, self.coordy, 76, 76])
            pygame.draw.rect(self.screen, (252, 3, 3), [self.coordx, self.coordy, 76, 76], 2)
        else:
            self.screen.blit(num, self.coords)
            pygame.draw.rect(self.screen, (252, 3, 3), [self.coordx, self.coordy, 76, 76], 2)