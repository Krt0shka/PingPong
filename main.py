import pygame
import config
import start

pygame.init()

screen = pygame.display.set_mode((config.WEIGHT, config.HEIGHT))
pygame.display.set_caption("Ping Pong")
pygame.display.set_icon(pygame.image.load("files/images/icon.png"))

fontT = pygame.font.SysFont("Arial", 40)
font = pygame.font.SysFont("Arial", 30)
fontS = pygame.font.SysFont("Arial", 20)

if __name__ == "__main__":
    start.start()