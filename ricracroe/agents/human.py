from ricracroe.agents.player import Player
from ricracroe.board import Board

class Human(Player):
    def __init__(self, name: str):
        self.name = name

    def move(self, state: Board) -> int:
        
        valid_moves = state.valid_moves()        
        # Pick from among the valid moves
        while True:
            state.render_board(placeholder=True)
            print(f"Valid choices are: {valid_moves}")
            choice = input("> ")
            if choice.isdigit() and int(choice) in valid_moves:
                return int(choice)
        
