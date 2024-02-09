import math
class coor():
    def __init__(self):
        self.x = int(input())
        self.y = int(input())
    def show(self):
        print("x = "+str(self.x))
        print("y = "+str(self.y))
    def move(self):
        self.x = int(input())
        self.y = int(input())
    def dist(self):
        x = int(input("coordinates of the second point x: "))
        y = int(input("coordinates of the second point y: "))
        print(math.sqrt((x - self.x)*(x - self.x)+(y - self.y)*(y - self.y)))
coordinates = coor()
coordinates.show()
coordinates.move()
coordinates.show()
coordinates.dist()

