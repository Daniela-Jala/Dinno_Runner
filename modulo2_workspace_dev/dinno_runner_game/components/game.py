import pygame
from dinno_runner_game.components.dinosaur import Dinosaur
from dinno_runner_game.components.clouds.cloud_manager import CloudManager
from dinno_runner_game.components.obstacles.cactus import Cactus
from dinno_runner_game.components.obstacles.obstacle_manager import ObstacleManager
from dinno_runner_game.components.obstacles.obstacle_manager_2 import ObstacleManager2
from dinno_runner_game.components.suns.sun_manager import SunManager
from dinno_runner_game.components.text import Text

from dinno_runner_game.utils.constants import BG, BG2, FPS, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SOUND, TITLE




class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_bg2 = 0
        self.y_pos_bg2 = 380
        self.death_count = 0
        self.cloud_manager = CloudManager()
        self.sun_manager = SunManager()
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.obstacle_manager_2 = ObstacleManager2()
        self.text = Text()
        pygame.mixer.init()
        self.start_sound = pygame.mixer.music.load(SOUND) 
        self.start_sound = pygame.mixer.music.play(-1)
        self.start_sound = pygame.mixer.music.set_volume(0.1)

    def run(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_r]:
            self.cloud_manager.update(self)
            self.sun_manager.update(self.game_speed)
            self.obstacle_manager.update(self.game_speed, self.player)
        self.obstacle_manager_2.update(self.game_speed, self.player)

        self.player.update(user_input)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((178, 255, 255))
        self.draw_background(self.screen)
        self.cloud_manager.draw(self.screen)
        self.sun_manager.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.obstacle_manager_2.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self, screen):
        user_input = pygame.key.get_pressed()
        image_width_bg2 = BG2.get_width()
        self.text.show(screen, 16, "Name:THE KING", pos_x = 555, pos_y = 20)
        self.screen.blit(BG2, (self.x_pos_bg2, self.y_pos_bg2))
        self.screen.blit(BG2, (image_width_bg2 + self.x_pos_bg2, self.y_pos_bg2))
        if user_input[pygame.K_r]:
            if self.x_pos_bg2 <= -image_width_bg2:
                self.screen.blit(BG2, (image_width_bg2 + self.x_pos_bg2, self.y_pos_bg2))
                self.x_pos_bg2 = 0
            self.x_pos_bg2 -= self.game_speed

        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if user_input[pygame.K_r]:
            if self.x_pos_bg <= -image_width:
                self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
                self.x_pos_bg = 0
            self.x_pos_bg -= self.game_speed
        
        
    
    

    
