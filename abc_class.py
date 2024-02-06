from abc import ABC, abstractmethod

class FamousSongs(ABC):
    @abstractmethod
    def artists(self):
        pass

    @abstractmethod
    def song_title(self):
        pass

