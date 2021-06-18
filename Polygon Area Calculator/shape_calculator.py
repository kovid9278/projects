class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return "Rectangle(width={}, height={})".format(self.width, self.height)
  # To change width
  def set_width(self, newWidth):
    self.width = newWidth

  # To change height
  def set_height(self, newHeight):
    self.height = newHeight
 
  # To calculate area
  def get_area(self):
    return self.width * self.height
  # To calculate perimeter
  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  # To calculate diagonal length
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  # To draw the shape
  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    shape = ""
    for i in range(self.height):
      shape += "*" * self.width + "\n"
    return shape
    '''picture = (("*" * self.width) + \n) * self.height 
    return picture'''

  # To calculate number of times that can fit inside
  def get_amount_inside(self, shape):
    return int(self.get_area() / shape.get_area())

# Creating subclass square 
class Square(Rectangle):
  def __init__(self, sideLength):
    self.width = sideLength
    self.height = sideLength

  def __str__(self):
    return "Square(side={})".format(self.width)
    
  def set_side(self, newSideLength):
    self.width = newSideLength
    self.height = newSideLength

