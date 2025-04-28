import pygame
import config

screen = pygame.display.set_mode((config.WEIGHT, config.HEIGHT))
pygame.display.set_caption("Ping Pong")
pygame.display.set_icon(pygame.image.load("files/images/icon.png"))

screen.fill(config.BACKGROUND_COLOR, (0, 0, 700, 500))


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
        if keys[pygame.K_w] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < 500 - 96:
            self.rect.y += self.speed

    def update2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 1:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < 500 - 96:
            self.rect.y += self.speed

player1 = Player(pygame.image.load("files/images/player1.png"), 5, 10, 200)
player2 = Player(pygame.image.load("files/images/player2.png"), 5, config.WEIGHT-40, 200)


clock = pygame.time.Clock()
game = True
while game:
    screen.fill(config.BACKGROUND_COLOR, (0, 0, 700, 500))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    player1.reset()
    player1.update1()

    player2.reset()
    player2.update2()

    clock.tick(config.FPS)
    pygame.display.flip()