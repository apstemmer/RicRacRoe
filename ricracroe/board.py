class Board:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
    
    
    # def __init__(self, b):
    #     self.board = [[c for c in r] for r in b]

    """
    Returns either:
      X - When X has won the game
      O - When O has won the game
      = - When the game has finished with a draw
      None - When the game is not in a terminal state
    """  
    def is_terminal(self):
        pass

    def valid_moves(self):
        pass

    def place(self, move: int, char: str):
        row = move // 3
        col = move % 3
        if move not in self.valid_moves():
            # Making an invalid move means you lose your turn ;)
            print("Trying to make an invalid move!")
        else:
            self.board[row][col] = char
