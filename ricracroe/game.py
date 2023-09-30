from ricracroe.agents import Player, Human
from ricracroe.board import Board

class Game:
    def __init__(self, p1: Player, p2: Player) -> None:
        self.p1 = p1 # Using X
        self.p2 = p2 # Using O
        self.board = Board()
        self.curr_player = p1

    def render_board(self) -> None:
        view = "\n"
        for row in self.board.board:
            view += " | ".join([str(n if n else ' ') for n in row])
            view += "\n"
        print(view)

    def play(self) -> None:
        print("### Beginning a game of RicRacRoe ###")
        while not self.board.is_terminal():
            print(f"Turn: {self.curr_player.name}")
            self.render_board()
            if self.curr_player == self.p1:
                move = self.p1.move(self.board)
                self.board.place(move, 'X')
                self.curr_player = self.p2
            else:
                move = self.p2.move(self.board)
                self.board.place(move, 'O')
                self.curr_player = self.p1
        self.render_board()
        final_state = self.board.is_terminal()
        if final_state == 'X':
            print(f"{self.p1.name} is the winner!!")
        elif final_state == 'O':
            print(f"{self.p2.name} is the winner!!")
        else:
            print("Game is a draw!")