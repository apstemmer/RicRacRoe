from ricracroe.agents import Player, Human
from ricracroe.board import Board

class Game:
    def __init__(self, p1: Player, p2: Player) -> None:
        self.p1 = p1 # Using X
        self.p2 = p2 # Using O
        self.board = Board(start_turn='X') 

    def play(self) -> None:
        
        print("### Beginning a game of RicRacRoe ###")
        
        while not self.board.is_terminal():
            
            if self.board.turn == 'X':
                print(f"Turn: {self.p1.name}")
                move = self.p1.move(self.board)
                self.board.place(move)
            else:
                print(f"Turn: {self.p2.name}")
                move = self.p2.move(self.board)
                self.board.place(move)

        self.board.render_board()
        final_state = self.board.is_terminal()
        
        if final_state == 'X':
            print(f"{self.p1.name} is the winner!!")
        elif final_state == 'O':
            print(f"{self.p2.name} is the winner!!")
        else:
            print("Game is a draw!")