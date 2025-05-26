import pygame.display
import config
from main import font, fontS, screen
from classes import Button
from screens import Menu

def settings():

    Opened = True

    title = font.render("Настройки", True, (0, 0, 0))


    back_button = Button.Button(
        (0, 0, 0),
        (129, 129, 129),
        config.WEIGHT // 2 - 100, 430, 200, 40,
        "Назад",
        fontS
    )

    ball_speed_label = fontS.render("Скорость мяча", True, (0, 0, 0))

    ball_speed1 = Button.Button(
        (0, 0, 0),
        config.B1C,
        200, 160, 90, 30,
        "1",
        fontS
    )
    ball_speed2 = Button.Button(
        (0, 0, 0),
        config.B2C,
        300, 160, 90, 30,
        "2",
        fontS
    )
    ball_speed3 = Button.Button(
        (0, 0, 0),
        config.B3C,
        400, 160, 90, 30,
        "3",
        fontS
    )

    player_speed_label = fontS.render("Скорость игроков", True, (0, 0, 0))

    player_speed1 = Button.Button(
        (0, 0, 0),
        config.P1C,
        200, 250, 90, 30,
        "1",
        fontS
    )
    player_speed2 = Button.Button(
        (0, 0, 0),
        config.P2C,
        300, 250, 90, 30,
        "2",
        fontS
    )
    player_speed3 = Button.Button(
        (0, 0, 0),
        config.P3C,
        400, 250, 90, 30,
        "3",
        fontS
    )

    while Opened:

        screen.fill("#FFFFFF")

        screen.blit(title, (config.WEIGHT // 2 - title.get_width() // 2, 50))

        back_button.draw()

        screen.blit(ball_speed_label, (config.WEIGHT // 2 - title.get_width() // 2, 120))

        ball_speed1.draw()
        ball_speed2.draw()
        ball_speed3.draw()

        screen.blit(player_speed_label, (config.WEIGHT // 2 - title.get_width() // 2, 215))

        player_speed1.draw()
        player_speed2.draw()
        player_speed3.draw()


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Opened = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.rect.collidepoint(event.pos):
                    Menu.start_menu()
                    Opened = False

                elif ball_speed1.rect.collidepoint(event.pos):
                    config.BALLSPEED = 3
                    ball_speed1.rect_color = "#66B2FF"
                    config.B1C = "#66B2FF"
                    ball_speed2.rect_color = "#0080FF"
                    config.B2C = "#0080FF"
                    ball_speed3.rect_color = "#0080FF"
                    config.B3C = "#0080FF"
                elif ball_speed2.rect.collidepoint(event.pos):
                    config.BALLSPEED = 5
                    ball_speed2.rect_color = "#66B2FF"
                    config.B2C = "#66B2FF"
                    ball_speed1.rect_color = "#0080FF"
                    config.B1C = "#0080FF"
                    ball_speed3.rect_color = "#0080FF"
                    config.B3C = "#0080FF"
                elif ball_speed3.rect.collidepoint(event.pos):
                    config.BALLSPEED = 7
                    ball_speed3.rect_color = "#66B2FF"
                    config.B3C = "#66B2FF"
                    ball_speed2.rect_color = "#0080FF"
                    config.B2C = "#0080FF"
                    ball_speed1.rect_color = "#0080FF"
                    config.B1C = "#0080FF"

                elif player_speed1.rect.collidepoint(event.pos):
                    config.PLAYERSPEED = 3
                    player_speed1.rect_color = "#66B2FF"
                    config.P1C = "#66B2FF"
                    player_speed2.rect_color = "#0080FF"
                    config.P2C = "#0080FF"
                    player_speed3.rect_color = "#0080FF"
                    config.P3C = "#0080FF"
                elif player_speed2.rect.collidepoint(event.pos):
                    config.PLAYERSPEED = 5
                    player_speed2.rect_color = "#66B2FF"
                    config.P2C = "#66B2FF"
                    player_speed1.rect_color = "#0080FF"
                    config.P1C = "#0080FF"
                    player_speed3.rect_color = "#0080FF"
                    config.P3C = "#0080FF"
                elif player_speed3.rect.collidepoint(event.pos):
                    config.PLAYERSPEED = 7
                    player_speed3.rect_color = "#66B2FF"
                    config.P3C = "#66B2FF"
                    player_speed2.rect_color = "#0080FF"
                    config.P2C = "#0080FF"
                    player_speed1.rect_color = "#0080FF"
                    config.P1C = "#0080FF"