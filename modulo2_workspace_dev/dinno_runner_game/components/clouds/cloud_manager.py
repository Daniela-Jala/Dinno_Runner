import random
import pygame

from dinno_runner_game.components.clouds.cloud import Cloud


class CloudManager:
    def __init__(self):
        self.clouds = []

    def update(self, game):
        if not self.clouds:
            self.clouds.append(Cloud())

        for cloud in self.clouds:
            cloud.update(game.game_speed, self.clouds)

    def draw(self, screen):
        for cloud in self.clouds:
            cloud.draw(screen)

    def reset(self):
        self.clouds = []