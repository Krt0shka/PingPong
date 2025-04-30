import config
from main import screen, font

class Counter:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0
        self.color = (0, 0, 0)
        self.screen = screen
        self.font = font
        self.text = self.font.render(f"{self.score1} : {self.score2}", True, self.color)
    def update(self):
        self.text = self.font.render(f"{self.score1} : {self.score2}", True, self.color)
        text_width = self.text.get_width()
        self.screen.blit(self.text, ((config.WEIGHT - text_width) // 2, 10))