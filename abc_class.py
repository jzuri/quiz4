from abc import ABC, abstractmethod

class FamousSongs(ABC):
    @abstractmethod
    def artists(self):
        pass

    @abstractmethod
    def song_title(self):
        pass

class Country(FamousSongs):
    def artists(self):
        print("Implementation of artists in Country")

    def song_title(self):
        print("Implementation of song_title in Country")

class Pop(FamousSongs):
    def artists(self):
        print("Implementation of artists in Pop")

    def song_title(self):
        print("Implementation of song_title in Pop")

# Example usage:
obj1 = Country()
obj1.artists()
obj1.song_title()

obj2 = Pop()
obj2.artists()
obj2.song_title()
