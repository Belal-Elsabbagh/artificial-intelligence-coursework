from rectangle import Rectangle


class Cuboid(Rectangle):
    height: float

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def __repr__(self):
        data_dict = {
            'length': self.length,
            'width': self.width,
            'height': self.height,
            'perimeter': self.perimeter(),
            'area': self.area(),
            'volume': self.volume()
        }
        return f"Cuboid: {data_dict}"

    def perimeter(self):
        return 4 * (self.height + self.width + self.length)

    def area(self):
        return (2 * (self.width * self.length)) + (2 * (self.length * self.height)) + (2 * (self.height * self.width))

    def volume(self):
        return self.height * self.width * self.length
