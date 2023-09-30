from ricracroe.agents.player import Player
from ricracroe.board import Board

import random

class Random(Player):
    def __init__(self, name: str):
        self.name = name
    
    def move(self, state: Board) -> int:
        valid_moves = state.valid_moves()

        return random.choice(valid_moves)
