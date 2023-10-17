
from controller.play import Game


game = Game(1000, 500, 25, 0.05)

while True:
    game.control()
