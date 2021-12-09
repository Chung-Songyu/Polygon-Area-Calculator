class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."

    pic = ""
    (width, height) = (self.width, self.height)
    for i in range(height):
      for i in range(width):
        pic += "*"
      pic += "\n"

    return pic

  def get_amount_inside(self, shape):
    return int(self.width / shape.width) * int(self.height / shape.height)

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side

  def set_side(self, side):
    self.width = side
    self.height = side

  def __str__(self):
    return "Square(side=" + str(self.width) + ")"

  def set_width(self, side):
    self.width = side

  def set_height(self, side):
    self.height = side

# Example
rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
