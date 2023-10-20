import math

class Point:
    def __init__(self, x=3, y=4):
        self.x = x
        self.y = y

    def show(self):
        print(f'{self.x} {self.y}')

    def move(self, x, y):
        self.x = x
        self.y = y
        print('New coordinates:', self.x, self.y)

    def dist(self, other_point):
        d = math.sqrt(pow((self.x - other_point.x), 2) + pow((self.y - other_point.y), 2))
        return d

p = Point()
p.show()


p.move(2, 2)


k = Point(1, 1)
k.show()
p.show()

distance = p.dist(k)
print(f'Distance between the two points: {distance}')

