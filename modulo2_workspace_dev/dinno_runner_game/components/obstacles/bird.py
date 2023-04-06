import random
from dinno_runner_game.components.obstacles.obstacle import Obstacle
from dinno_runner_game.utils.constants import BIRD, SCREEN_HEIGHT, SCREEN_WIDTH


class Bird(Obstacle):
    def __init__(self):
        image = BIRD[0]
        super().__init__(image)
        self.rect.x = random.randint(1200, 1200)
        self.rect.y = random.randint(95, 300)
        self.step = 0

    def update(self, game_speed, obstacles):
        super().update(game_speed, obstacles)
        self.image = BIRD[self.step // 10]
        self.step += 1
        if self.step >= 20:
            self.step = 0