from ricracroe.agents import Player, Human
from ricracroe.board import Board

class Game:
    def __init__(self, p1: Player, p2: Player) -> None:
        self.p1 = p1
        self.p2 = p2
        self.board = Board()
        self.curr_player = p1

    def play(self) -> None:
        while not self.board.is_terminal():
            if self.curr_player == self.p1:
                self.p1.move(self.board)
                self.curr_player = self.p2
            else:
                self.p2.move(self.board)
                self.curr_player = self.p1