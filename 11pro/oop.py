class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        print(f'({self.x};{self.y})')


class Line:
    def __init__(self, point1, point2):
        self.start = point1
        self.end = point2

    def get_length(self):
        b = self.start.x - self.end.x
        a = self.start.y - self.end.y
        length = (a ** 2 + b ** 2) ** 0.5
        print(length)



point1 = Point(5,3)
point2 = Point(3,5)
line = Line(point1, point2)
line.get_length()
