import pygame
from main import screen

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img: pygame.Surface, speed, x, y):
        super().__init__()
        self.image = img
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))