import pygame
import random
import config
from classes.GameSprite import GameSprite

class Ball(GameSprite):
    def __init__(self, img: pygame.Surface, speed, x, y):
        super().__init__(img, speed, x, y)
        self.direction_x = random.choice([-1, 1])
        self.direction_y = random.choice([-1, 1])

    def update(self):
        self.rect.x += self.speed * self.direction_x
        self.rect.y += self.speed * self.direction_y
        if self.rect.y <= 1 or self.rect.y >= config.HEIGHT - 61:
            self.direction_y *= -1