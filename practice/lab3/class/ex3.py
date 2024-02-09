class Shape:
  def __init__(self):
    pass

  def area(self):
    print(0)
class Square(Shape):
  def __init__(self, length,width):
    super().__init__()
    self.length = length
    self.width = width

  def area(self):
    area = self.length * self.width
    print(area)
square = Square(26,199)
square.area()
