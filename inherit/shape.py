class shape:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Rectangle(shape):
	def getArea(self):
		return self.x*self.y

class Circle(shape):
	def __init__(self,r):
		self.r = r

	def getArea(self):
		return 3.14*self.r*self.r

class Square(Rectangle):
	def __init__(self,b):
		self.b = b
	def getArea(self):
		return self.b*self.b

x,y=input().split()
s1 = Rectangle(int(x),int(y))
print(s1.getArea())
r=input()
s2 = Circle(int(r))
print(s2.getArea())
b=input()
s3 = Square(int(b))
print(s3.getArea())


	
