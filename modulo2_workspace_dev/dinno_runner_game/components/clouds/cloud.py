import random

from pygame import Surface
from pygame.sprite import Sprite

from dinno_runner_game.utils.constants import CLOUD, SCREEN_WIDTH



class Cloud(Sprite):
    def __init__(self):
        cloud_type = random.randint(0,2)
        self.image = CLOUD[cloud_type]
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(400, 600)
        self.rect.y = 110

    def update(self, game_speed, clouds):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            clouds.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))