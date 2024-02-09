class String:
  def __init__(self):
    self.string = ""

  def getString(self):
    self.string = input()

  def printString(self):
    print(self.string.upper())
string = String()
string.getString()
string.printString()
