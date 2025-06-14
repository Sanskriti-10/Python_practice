#8. Create a Python class Rectangle with attributes length and width. Add methods to compute area and perimeter.

class Rectangle:
  def __init__(self,length,breadth):
    self.length=length
    self.breadth=breadth

  def area(self):
    return self.length*self.breadth  
  def perimeter(self):
    return (self.length+self.breadth)*2
  

r1=Rectangle(5,4)  
print(r1.area()) 
print(r1.perimeter())
