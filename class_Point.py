class Human:
    pass


class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, point):
        if not isinstance(point, Point):
            raise TypeError('Please provide point instance')
        return Point(self.x + point.x, self.y + point.y)

    def __iadd__(self, other):
        if not isinstance(other, Point):
            raise TypeError('Please provide point instance')
        self.x += other.x
        self.y += other.y
        return self

    __add__ = add
    # def __add__(self, other):
    #     return self.add(other)

    def __str__(self):
        return f'<Point {self.x}, {self.y}>'


p = Point(2, 3)
p2 = Point(5, -7)
p3 = p + p2
p3 = p.__add__(p2)
print(p.add(p2))
p3 += Point(1, 2)
# p3 = p3.__iadd__(Point(1, 2))
print(p3)
# h = Human()
# l =[]
# print(isinstance(l, (Point, Human)))
# print(p.x, p.y)

