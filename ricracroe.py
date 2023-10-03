from ricracroe.agents import Human, Random
from ricracroe.game import Game

p1 = Human(name="Arthur")
p2 = Random(name="Anton A.I.")
game = Game(p1, p2)
game.play()