import pygame

from dinno_runner_game.utils.constants import SCREEN_WIDTH

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, image: pygame.Surface):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.passed = False
        self.collided = False
        

    def update(self, game_sped, obstacles):
        self.rect.x -= game_sped
        if self.rect.x < -self.rect.width:
            obstacles.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def collide(self, player):
        if self.rect.colliderect(player.rect) and not self.collided:
            self.collided = True
            return True
        return False