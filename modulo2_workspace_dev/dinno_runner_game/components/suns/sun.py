import random

from pygame import Surface
from pygame.sprite import Sprite

from dinno_runner_game.utils.constants import SUN,SCREEN_WIDTH



class Sun(Sprite):
    def __init__(self):
        self.image = SUN
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 0

    def update(self, game_speed, suns):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            suns.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))