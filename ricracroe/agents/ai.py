from ricracroe.agents.player import Player
from ricracroe.board import Board

class AI(Player):
    def __init__(self, name:str):
        self.name = name

    def state_value(self, state:Board, agent='X') -> int:
        is_terminal = state.is_terminal()
        opponent = 'X' if agent == 'O' else 'O'
        
        # Base case
        if is_terminal == agent:
            return 1
        elif is_terminal == opponent:
            return -1
        elif is_terminal == '=':
            return 0
        
        # If not a terminal state
        scores = {}
        for m in state.valid_moves():
            sub_board: Board = state.copy_of()
            sub_board.place(m)
            scores[m] = self.state_value(sub_board, agent)
        
        return max(scores.values())

    def move(self, state:Board) -> int:
        
        move_scores = {}
        for mv in state.valid_moves():
            sub_board: Board = state.copy_of()
            sub_board.place(mv)
            move_scores[mv] = self.state_value(sub_board, agent=state.turn)
        
        return max(move_scores.items(), key = lambda m: m[1])[0]


