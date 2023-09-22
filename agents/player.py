from abc import ABC, abstractmethod

class Player(ABC):

    @abstractmethod
    def move(self, state, moves):
        return 