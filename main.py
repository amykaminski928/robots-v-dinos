from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
from battlefield import Battlefield
#instantiate weapon
#active_weapon=Weapon("Fangs", 5)
#instantiate robot
active_robot=Robot("Chewy")


#instantiate Dinosaur
active_dino=Dinosaur("Blue", 10)


#dino attack
active_dino.attack(active_robot)
active_robot.attack(active_dino)