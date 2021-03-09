import logging


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

    def __eq__(self, other):
        print('Called eq')
        if not isinstance(other, Point):
            logging.warning('Please provide Point instance for comparisson')
            return False
            # raise TypeError('Please provide point instance')
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        print('Called gt')
        if not isinstance(other, Point):
            raise TypeError('Please provide point instance')
        return self.x > other.x and self.y > other.y

    def __str__(self):
        return f'<Point {self.x}, {self.y}>'


p1 = Point(2, 3)
p2 = Point(1, 2)
# print(p1 == p2)
# print(p1 is p2)

print(p1 != p2)

