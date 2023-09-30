class Board:
    
    winners = [
        # Diagonal
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)],
        # Horizontal
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        # Vertical
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)]
    ] 

    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    """
    Returns either:
      X - When X has won the game
      O - When O has won the game
      = - When the game has finished with a draw
      None - When the game is not in a terminal state
    """  
    def is_terminal(self):
       
        # Check for a clear winner
        for candidate in winners:
            line = [self.board[c[0]][c[1]] for c in candidate]
            if line == ['X', 'X', 'X']:
                return 'X'
            elif line == ['O', 'O', 'O']:
                return 'O'
          
        # If no further moves and no winner - it is a draw. 
        if self.valid_moves == []:
           return '='
        
        # Otherwise, the show must go on!
        return None

    def valid_moves(self) -> list[int]:
        moves = []
        for m in range(9):
            row, col = self._int_to_rc(m)
            if not self.board[row][col]:
                moves.append(m)
        return moves
    
    def _int_to_rc(self, index: int) -> tuple[int, int]:
        return (index // 3, index % 3) 

    def place(self, move: int, char: str) -> None:
        row, col = self._int_to_rc(move)
        if move not in self.valid_moves():
            # Making an invalid move means you lose your turn ;)
            print("Trying to make an invalid move!")
        else:
            self.board[row][col] = char
