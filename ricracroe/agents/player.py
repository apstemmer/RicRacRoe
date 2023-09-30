from abc import ABC, abstractmethod
from ricracroe.board import Board

class Player(ABC):

    @abstractmethod
    def move(self, state: Board):
        return 