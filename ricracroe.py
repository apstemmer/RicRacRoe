from ricracroe.agents import Human, Random, AI
from ricracroe.game import Game

p1 = Human(name="Arthur")
p2 = AI(name="Anton A.I.")
game = Game(p1, p2)
game.play()