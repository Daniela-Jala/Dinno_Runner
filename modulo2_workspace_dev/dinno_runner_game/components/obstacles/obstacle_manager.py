from dinno_runner_game.components.obstacles.obstacle import Obstacle
from dinno_runner_game.components.obstacles.cactus import Cactus
from dinno_runner_game.components.text import Text


class ObstacleManager():
    def __init__(self):
        self.obstacles = []# se agarrra un obstaculo se guardara en esta lista vacia y cuando salga de la pantalla
                           #se eliminara de esta lista
        self.cactus_bang = 0
        self.cactus_count = 0
        self.text = Text()

    def update(self, game_speed, player):
        #generamos los obstaculos cuando no tengamos ninguno
        if not self.obstacles:
            self.obstacles.append(Cactus()) # y como tenemos una lista vacia ahi entra las imagenes de los obstaculos
            self.cactus_count = self.cactus_count + 1

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)#le pasamos el juego y los obstaculos y se actualizaran
            
            if obstacle.collide(player):
                self.cactus_bang = self.cactus_bang + 1

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        self.text.show(screen, 16, f"Cactus Deaths: {self.cactus_bang}", pos_x = 135, pos_y = 50)
        self.text.show(screen, 16, f"Cactus Number: {self.cactus_count}", pos_x = 135, pos_y = 80)




        
        
        
        