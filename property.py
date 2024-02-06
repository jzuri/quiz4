class Square:
    def __init__(self, length):
        self._length = length

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return 2 * self._width

    @property
    def area(self):
        return self._width * self._length

# Example usage:
if __name__ == "__main__":
    # Creating Square class
    my_square = Square(length=5)

