import random
from dinno_runner_game.components.obstacles.obstacle import Obstacle
from dinno_runner_game.components.obstacles.cactus import Cactus
from dinno_runner_game.components.text import Text
from dinno_runner_game.components.obstacles.bird import Bird


class ObstacleManager():
    def __init__(self):
        self.obstacles = []# se agarrra un obstaculo se guardara en esta lista vacia y cuando salga de la pantalla
                           #se eliminara de esta lista
        self.cactus_bang = 0
        self.cactus_count = 0
        self.cactus_evaded = 0
        self.bird_bang = 0
        self.bird_count = 0
        self.bird_evaded = 0
        self.score_cactus = 0
        self.score_bird = 0
        self.score = 0
        self.text = Text()

    def update(self, game_speed, player):
        #generamos los obstaculos cuando no tengamos ninguno
        if not self.obstacles:
            probability = random.randint(0, 7)

            if probability <= 6:
                self.obstacles.append(Cactus()) # y como tenemos una lista vacia ahi entra las imagenes de los obstaculos
                self.cactus_count +=  1

            else:
                self.obstacles.append(Bird())
                self.bird_count += 1

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)#le pasamos el juego y los obstaculos y se actualizaran
            
            if obstacle.rect.right < player.rect.left and not obstacle.passed:
                obstacle.passed = True
                self.cactus_evaded += 1
                self.score_cactus = self.score_cactus + 100

            if obstacle.collide(player):
                self.cactus_bang += 1
                self.score_cactus = self.score_cactus - 50

        for bird in self.obstacles:
            bird.update(game_speed, self.obstacles)

            if bird.rect.right < player.rect.left and not obstacle.passed:
                obstacle.passed = True
                self.bird_evaded += 1
                self.score_bird = self.score_bird + 75

            if obstacle.collide(player):
                self.bird_bang += 1
                self.score_bird = self.score_bird - 25
            
        self.score = self.score_cactus + self.score_bird
    
    def draw(self, screen):

        for obstacle in self.obstacles:
            obstacle.draw(screen)
        self.text.show(screen, 13, f"Cactus Deaths: {self.cactus_bang}", pos_x = 110, pos_y = 20)
        self.text.show(screen, 13, f"Cactus Number: {self.cactus_count}", pos_x = 110, pos_y = 40)
        self.text.show(screen, 13, f"Cactus Evaded: {self.cactus_evaded}", pos_x = 110, pos_y = 60)
        self.text.show(screen, 13, f"Bird Deaths: {self.bird_bang}", pos_x = 98, pos_y = 90)
        self.text.show(screen, 13, f"Bird Number: {self.bird_count}", pos_x = 98, pos_y = 110)
        self.text.show(screen, 13, f"Bird Evaded: {self.bird_evaded}", pos_x = 98, pos_y = 130)
        self.text.show(screen, 13, f"Score: {self.score}", pos_x = 555, pos_y = 80)


