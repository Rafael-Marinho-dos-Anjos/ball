
from controller.play import Game, is_pressed


game = Game(1000, 500, 25, 0.05)

while not is_pressed("esc"):
    game.control()
