import pygame
from classes.GameSprite import GameSprite

class Player(GameSprite):
    def update1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 500 - 130:
            self.rect.y += self.speed

    def update2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 500 - 130:
            self.rect.y += self.speed