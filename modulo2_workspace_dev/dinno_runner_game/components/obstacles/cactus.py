import random
from dinno_runner_game.components.obstacles.obstacle import Obstacle
from dinno_runner_game.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class Cactus(Obstacle):
    def __init__(self):
        cactus = [SMALL_CACTUS, LARGE_CACTUS]
        cactus_var = random.randint(0, 2) # se le da ese rango porque aleatoriamente se elegira una de esas 2 
                                            # posiciones y aparece una de las 2 imagenes de cactus
        cactus_type = random.choice(cactus)
        image = cactus_type[cactus_var]
        super().__init__(image) #el super llama a la clase padre y ejecuta el metodo que se necesit
        if cactus_type == SMALL_CACTUS:
            self.rect.y = 325
        else:
            self.rect.y = 300
        cactus_type = random.randint(0,2) 
                                          
        image = SMALL_CACTUS[cactus_type]