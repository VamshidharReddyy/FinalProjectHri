import pygame

class cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False
        self.font = pygame.font.Font(None, 36)

    def get_value(self):
        return self.value

    def draw(self):
        cell_size = self.screen.get_width() // 9
        x = self.col * cell_size
        y = self.row * cell_size

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, cell_size, cell_size), 3)

        if self.value != 0:
            text = self.font.render(str(self.value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
            self.screen.blit(text, text_rect)

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.value = value

