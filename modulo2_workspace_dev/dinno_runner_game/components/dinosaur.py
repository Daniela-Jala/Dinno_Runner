import pygame
from pygame.sprite import Sprite

from dinno_runner_game.utils.constants import  DINO_START, DUCKING, JUMPING, RUNNING, SOUND_JUMP, SOUND_DUCKING

DINO_RUNNING = "running"
DINO_JUMPING = "jumping"
DINO_DUCKING = "ducking"
DINO_START_IMG = DINO_START

class Dinosaur(Sprite):
    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 310
        self.step = 0
        self.action = DINO_START_IMG
        self.jump_velocity = 8.5
        self.playing_sound = False
        self.jump_sound = pygame.mixer.Sound(SOUND_JUMP)
        self.duck_sound = pygame.mixer.Sound(SOUND_DUCKING)
    
    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()

        if user_input[pygame.K_DOWN] or user_input[pygame.K_d]:
            if self.action == DINO_JUMPING:
                self.jump()
            else:
                self.action = DINO_DUCKING
                if not self.playing_sound:
                    self.duck_sound.play()
                    self.duck_sound.set_volume(0.1)
                    self.playing_sound = True

        elif self.action != DINO_JUMPING:
            if user_input[pygame.K_j] or user_input[pygame.K_SPACE]:
                self.jump_sound.play()
                self.jump_sound.set_volume(0.1)
                self.action = DINO_JUMPING
            elif user_input[pygame.K_d] or user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            elif user_input[pygame.K_r]:
                self.playing_sound = False
                self.action = DINO_RUNNING
            else:
                self.action = DINO_START_IMG

        if self.step >= 10:
            self.step = 0

    def run(self):
        self.image = RUNNING[0] if self.step < 5 else RUNNING[1]
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 310
        self.step = self.step + 1

    def jump(self):

        self.image = JUMPING
        self.rect.y = self.rect.y - self.jump_velocity * 4 # el jump_velocity se multiplicara por 4 va 
        self.jump_velocity = self.jump_velocity -0.8       #a ser la cantidad de pixeles que se va a mover y se le resta 
                                                           #una velocidad positiva para que el objeto se mueva hacia arriba
                                                           #y cuando la velocidad sea negativa se movera hacia abajo
        if self.jump_velocity < - 8.5: # se restablece el valor y ya no saltara 
            self.jump_velocity = 8.5
            self.action = DINO_RUNNING
            self.rect.y = 310

    def duck(self):
        self.image = DUCKING[0] if self.step < 5 else DUCKING[1]
        self.rect = self.image.get_rect()
        self.rect.x = 80
        self.rect.y = 350
        self.step = self.step + 1

    def draw(self, screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))

    def collitions(self):

        pass
            
        