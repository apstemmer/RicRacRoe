from ricracroe.agents.player import Player
from ricracroe.board import Board

class Human(Player):
    def __init__(self):
        pass

    def move(self, state: Board):
        valid_moves = state.valid_moves()
        return valid_moves[0]