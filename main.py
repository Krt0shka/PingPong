import pygame

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Ping Pong")
#pygame.display.set_icon(pygame.image.load("files/images/icon.png"))

background = pygame.transform.scale(pygame.image.load("files/images/bg.png"), (700, 500))


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

class Player(GameSprite):
    def update1(self):
        keys = pygame.key.get_pressed()

    def update2(self):
        keys = pygame.key.get_pressed()