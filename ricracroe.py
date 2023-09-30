from ricracroe.agents.human import Human
from ricracroe.game import Game

p1 = Human(name="Player1")
p2 = Human(name="Player2")
game = Game(p1, p2)
game.play()