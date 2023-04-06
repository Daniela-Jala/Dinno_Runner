import random

import pygame

from dinno_runner_game.components.suns.sun import Sun



class SunManager:
    def __init__(self):
        self.suns = []

    def update(self, game_speed):
        if not self.suns:
            self.suns.append(Sun())

        for sun in self.suns:
            sun.update(game_speed, self.suns)

    def draw(self, screen):
        for sun in self.suns:
            sun.draw(screen)

    def reset(self):
        self.suns = []