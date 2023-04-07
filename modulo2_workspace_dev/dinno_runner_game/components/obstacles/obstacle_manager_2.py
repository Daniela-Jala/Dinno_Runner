from dinno_runner_game.components.obstacles.bird import Bird
from dinno_runner_game.components.text import Text
from dinno_runner_game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class ObstacleManager2():
    def __init__(self):
        self.obstacles = []# se agarrra un obstaculo se guardara en esta lista vacia y cuando salga de la pantalla
                           #se eliminara de esta lista
        self.bird_bang = 0
        self.bird_count = 0
        self.bird_evaded = 0
        self.score = 0
        self.max_score = 0
        self.text = Text()

    def update(self, game_speed, player):
        #generamos los obstaculos cuando no tengamos ninguno
        if not self.obstacles:
            self.obstacles.append(Bird()) # y como tenemos una lista vacia ahi entra las imagenes de los obstaculos
            self.bird_count += 1
                
        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)#le pasamos el juego y los obstaculos y se actualozara

            if obstacle.collide(player):
                self.bird_bang += 1
                self.score = self.score - 100
            elif obstacle.rect.right < player.rect.left and not obstacle.passed:
                obstacle.passed = True
                self.bird_evaded += 1
                self.score = self.score + 100

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        #self.text.show(screen, 13, f"Bird Deaths: {self.bird_bang}", pos_x = 98, pos_y = 90)
        #self.text.show(screen, 13, f"Bird Number: {self.bird_count}", pos_x = 98, pos_y = 110)
        #self.text.show(screen, 13, f"Bird Evaded: {self.bird_evaded}", pos_x = 98, pos_y = 130)

