import random, time
import pygame
import config

pygame.init()

screen = pygame.display.set_mode((config.WEIGHT, config.HEIGHT))
pygame.display.set_caption("Ping Pong")
pygame.display.set_icon(pygame.image.load("files/images/icon.png"))

screen.fill(config.BACKGROUND_COLOR, (0, 0, 700, 500))

font = pygame.font.SysFont("Arial", 30)


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

class Counter:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.color = (0, 0, 0)
        self.text = font.render(f"{self.score1} : {self.score2}", True, self.color)
    def update(self):
        self.text = font.render(f"{self.score1} : {self.score2}", True, self.color)
        screen.blit(self.text, (config.WEIGHT // 2 - 50, 10))


player1 = Player(pygame.image.load("files/images/player1.png"), 5, 10, 200)
player2 = Player(pygame.image.load("files/images/player2.png"), 5, config.WEIGHT-40, 200)
ball = Ball(pygame.image.load("files/images/ball.png"), 5, config.WEIGHT//2, config.HEIGHT//2)
counter = Counter()

game = True
pause = False

clock = pygame.time.Clock()

last_pause_time = 0

while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                curr_time = pygame.time.get_ticks()
                if curr_time - last_pause_time >= 500 and pause == False:   #на паузу
                    pause = not pause
                    last_pause_time = curr_time
                    pause_text = font.render("ПАУЗА", True, (0, 0, 0))
                    screen.blit(pause_text, (config.WEIGHT // 2 - 50, config.HEIGHT // 2 - 50))
                else:                                                       #с паузы
                    pause = not pause


    if not pause:

        screen.fill(config.BACKGROUND_COLOR, (0, 0, 700, 500))
        counter.update()

        player1.reset()
        player1.update1()

        player2.reset()
        player2.update2()

        if pygame.sprite.collide_rect(ball, player1) or pygame.sprite.collide_rect(ball, player2):
            ball.direction_x *= -1

        if ball.rect.x < 15:
            counter.score2 += 1
            ball.rect.x = config.WEIGHT // 2
            ball.rect.y = config.HEIGHT // 2
            ball.direction_x *= -1
            ball.direction_y *= random.choice([-1, 1])
        if ball.rect.x > config.WEIGHT - 60:
            counter.score1 += 1
            ball.rect.x = config.WEIGHT // 2
            ball.rect.y = config.HEIGHT // 2
            ball.direction_x *= -1
            ball.direction_y *= random.choice([-1, 1])

        ball.reset()
        ball.update()

    clock.tick(config.FPS)
    pygame.display.flip()