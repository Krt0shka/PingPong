import pygame
import random
from classes import Player, Counter, Ball, Button
from screens import Menu
import config
from main import screen, font, fontS

def game():

    clock = pygame.time.Clock()

    mixer = pygame.mixer
    mixer.init()
    mixer.music.load("files/sounds/music.mp3")
    mixer.music.set_volume(0.1)
    hit_sound = mixer.Sound("files/sounds/hit.flac")
    hit_sound.set_volume(0.1)

    player1 = Player.Player(pygame.image.load("files/images/player1.png"), 5, 10, 200)
    player2 = Player.Player(pygame.image.load("files/images/player2.png"), 5, config.WEIGHT - 37, 200)
    ball = Ball.Ball(pygame.image.load("files/images/ball.png"), 5, config.WEIGHT // 2, config.HEIGHT // 2)
    counter = Counter.Counter()

    in_menu_button = Button.Button(
        (0, 0, 0),
        (129, 129, 129),
        5, 5, 100, 30,
        "В Меню",
        fontS
    )

    game = True
    pause = False
    last_pause_time = 0

    while game:

        mixer.music.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    curr_time = pygame.time.get_ticks()
                    if curr_time - last_pause_time >= 500 and pause == False:  # на паузу
                        pause = not pause
                        last_pause_time = curr_time
                        pause_text = font.render("ПАУЗА", True, (0, 0, 0))
                        screen.blit(pause_text, (config.WEIGHT // 2 - 50, config.HEIGHT // 2 - 50))
                    else:  # с паузы
                        pause = not pause
                elif event.key == pygame.K_ESCAPE:
                    Menu.start_menu()
                    game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if in_menu_button.rect.collidepoint(event.pos):
                    Menu.start_menu()
                    game = False

        if not pause:

            screen.fill(config.BACKGROUND_COLOR1, (0, 0, config.WEIGHT // 2, config.HEIGHT))
            screen.fill(config.BACKGROUND_COLOR2, (config.WEIGHT // 2, 0, config.WEIGHT, config.HEIGHT))
            counter.update()

            player1.reset()
            player1.update1()

            player2.reset()
            player2.update2()

            in_menu_button.draw()

            if pygame.sprite.collide_rect(ball, player1) or pygame.sprite.collide_rect(ball, player2):
                ball.direction_x *= -1
                hit_sound.play()

            if ball.rect.x < 35:
                counter.score2 += 1
                ball.rect.x = config.WEIGHT // 2
                ball.rect.y = config.HEIGHT // 2
                ball.direction_x *= -1
                ball.direction_y *= random.choice([-1, 1])
            if ball.rect.x > config.WEIGHT - 90:
                counter.score1 += 1
                ball.rect.x = config.WEIGHT // 2
                ball.rect.y = config.HEIGHT // 2
                ball.direction_x *= -1
                ball.direction_y *= random.choice([-1, 1])

            ball.reset()
            ball.update()

        clock.tick(config.FPS)
        pygame.display.flip()