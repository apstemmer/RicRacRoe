from ricracroe.agents.player import Player
from ricracroe.board import Board

class Human(Player):
    def __init__(self, name: str):
        self.name = name

    def move(self, state: Board) -> int:
        valid_moves = state.valid_moves()
        # Pick from among the valid moves
        return valid_moves[0]
