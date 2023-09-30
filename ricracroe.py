from ricracroe.agents import Human, Random
from ricracroe.game import Game

p1 = Random(name="Player1")
p2 = Random(name="Player2")
game = Game(p1, p2)
game.play()