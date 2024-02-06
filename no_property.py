class Square:
    def __init__(self, length):
        self._length = length

    def get_length(self):
        return self._length

    def get_width(self):
        return 2 * self._width

    def get_area(self):
        return self._width * self._length

# Example usage:
if __name__ == "__main__":
    # Square class 2.0
    my_square = Square(length=5)


