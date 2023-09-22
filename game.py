from agents import Player, Human

class Game:
    def __init__(self, p1: Player, p2: Player) -> None:
        pass

    def play(self) -> None:
        pass

if __name__ == '__main__':
    p1 = Human()
    p2 = Human()
    game = Game(p1, p2)
    game.play()