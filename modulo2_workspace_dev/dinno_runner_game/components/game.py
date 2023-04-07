import pygame
from dinno_runner_game.utils.constants import DINO_START, DINO_DEAD, GAME_OVER
from dinno_runner_game.components.dinosaur import Dinosaur
from dinno_runner_game.components.clouds.cloud_manager import CloudManager
from dinno_runner_game.components.obstacles.cactus import Cactus
from dinno_runner_game.components.obstacles.obstacle_manager import ObstacleManager
from dinno_runner_game.components.suns.sun_manager import SunManager
from dinno_runner_game.components.text import Text

from dinno_runner_game.utils.constants import BG, BG2, FPS, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SOUND, TITLE, FONT_STYLE, DINO_START
from dinno_runner_game.components.obstacles.obstacle_manager_2 import ObstacleManager2


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
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
        self.obstacle_manager2 = ObstacleManager2()
        self.text = Text()
        pygame.mixer.init()
        self.start_sound = pygame.mixer.music.load(SOUND) 
        self.start_sound = pygame.mixer.music.play(-1)
        self.start_sound = pygame.mixer.music.set_volume(0.1)

    def run(self):
        self.executing = True
        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def start_game(self):
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        if user_input[pygame.K_r]:
            self.cloud_manager.update(self)
            self.sun_manager.update(self.game_speed)
            self.obstacle_manager.update(self.game_speed, self.player, self, self.screen)
        #self.obstacle_manager2.update(self.game_speed, self.player)

        self.player.update(user_input)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((178, 255, 255))
        self.draw_background(self.screen)
        self.cloud_manager.draw(self.screen)
        self.sun_manager.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self, screen):
        user_input = pygame.key.get_pressed()
        image_width_bg2 = BG2.get_width()
        self.text.show(screen, 16, "Name:", pos_x = 480, pos_y = 20, color = (60,60,60))
        self.text.show(screen, 16, "THE KING", pos_x = 580, pos_y = 20, color = (255,60,60))
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

    def show_menu(self):
        self.screen.fill((178, 255, 255))
        image_width_bg2 = BG2.get_width()
        self.screen.blit(BG2, (self.x_pos_bg2, self.y_pos_bg2))
        self.screen.blit(BG2, (image_width_bg2 + self.x_pos_bg2, self.y_pos_bg2))
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))

        if not self.death_count:
            font = pygame.font.Font(FONT_STYLE, 32)
            text = font.render("PRESS ANY KEY TO START", True, (0, 0, 0))
            text_rect = text.get_rect()
            half_screen_width = SCREEN_WIDTH // 2
            half_screen_height = SCREEN_HEIGHT // 2
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text,text_rect)
            self.screen.blit(DINO_START,(half_screen_height + 150 ,half_screen_width - 500))
        else:
            pass
        pygame.display.update()
        self.handle_menu_events()

    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False

            if event.type == pygame.KEYDOWN:
                self.start_game()

    
    

    
