import pygame
from main import screen

class Button:
    def __init__(self, tcolor: tuple, rcolor: tuple, x: int, y: int, w: int, h: int, text: str, font):
        self.text_color = tcolor
        self.rect_color = rcolor
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.text = self.font.render(text, True, self.text_color)

    def draw(self):
        pygame.draw.rect(screen, self.rect_color, self.rect)
        screen.blit(self.text, (
            self.rect.centerx - self.text.get_width() // 2,
            self.rect.centery - self.text.get_height() // 2
        ))