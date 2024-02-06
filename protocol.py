from typing import Protocol, abstractmethod

class FamousSongs(Protocol):
    @abstractmethod
    def artists(self) -> None:
        pass

    @abstractmethod
    def song_title(self) -> None:
        pass

class Country:
    def artists(self) -> None:
        print("Implementation of artists in Country")

    def song_title(self) -> None:
        print("Implementation of song_title in Country")

class Pop:
    def artists(self) -> None:
        print("Implementation of artists in Pop")

    def method2(self) -> None:
        print("Implementation of song_title in Pop")

# Example usage:
obj1 = Country()
obj1.artists()
obj1.song_title()

obj2 = Pop()
obj2.artists()
obj2.song_title()
