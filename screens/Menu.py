import pygame
import config
from screens import Game, Settings
from classes import Button
from main import screen, font, fontS, fontT

def start_menu():

    start_button = Button.Button(
        (255, 255, 255),
        (0, 0, 0),
        config.WEIGHT // 2 - 100, 250, 200, 60,
        "Старт",
        font
    )

    settings_button = Button.Button(
        (255, 255, 255),
        (70, 70, 70),
        config.WEIGHT // 2 - 100, 320, 200, 40,
        "Настройки",
        fontS
    )

    waiting = True
    while waiting:
        screen.fill("#FFFFFF")

        title = fontT.render("Пинг Понг", True, (0, 0, 0))
        screen.blit(title, (config.WEIGHT // 2 - title.get_width() // 2, 150))

        start_button.draw()
        settings_button.draw()

        control_p1 = fontS.render("Игрок 1: Вверх - W, вниз - S", True, (0, 0, 0))
        control_p2 = fontS.render("Игрок 2: Вверх - ↑, вниз - ↓", True, (0, 0, 0))
        screen.blit(control_p1, (5, config.HEIGHT - 60))
        screen.blit(control_p2, (5, config.HEIGHT - 30))

        game_version = fontS.render(f"Версия игры: {config.VERSION}", True, (0, 0, 0))
        screen.blit(game_version, (config.WEIGHT - game_version.get_width() - 5, config.HEIGHT - 30))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Game.game()
                    waiting = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.rect.collidepoint(event.pos):
                    Game.game()
                    waiting = False
                elif settings_button.rect.collidepoint(event.pos):
                    Settings.settings()
                    waiting = False