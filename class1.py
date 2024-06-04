class Rectangle:
	def __init__(self, w, h): 
		self.width = w 
		self.height = h

	def __eq__(self, other):
		return self.width == other.width and self.height == other.height
r1 = Rectangle(3, 5) 
r2 = Rectangle(4, 6) 
r3 = Rectangle(3, 5)
print(r1 == r3)
