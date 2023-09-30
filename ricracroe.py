from ricracroe.agents.human import Human
from ricracroe.game import Game

p1 = Human()
p2 = Human()
game = Game(p1, p2)
game.play()