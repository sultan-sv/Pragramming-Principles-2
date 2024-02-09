class Shape:
  def __init__(self):
    pass

  def area(self):
    print(0)
class Square(Shape):
  def __init__(self, length):
    super().__init__()
    self.length = length

  def area(self):
    area = self.length * self.length
    print(area)
square = Square(26)
square.area()
