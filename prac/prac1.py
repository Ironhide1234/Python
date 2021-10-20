class Rectangle:
    def __init__(self,width = 1, height = 1):
        self.height  = height      
        self.width = width
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height    
    @height.setter
    def height(self,height):
        if height <= 20 and height > 0:
            self.__height = height 
        else:
            raise ValueError
    @width.setter
    def width(self,width):
        if width <= 20 and width > 0:
            self.__width = width 
        else:
            raise ValueError
    def user(self):
        return f'Your width: {self.__width}\nYour height: {self.__height}'       
    def perimeter(self):
        return f'Perimeter: {(self.__width + self.height) * 2}'
    def area(self):
        return f'Area: {(self.__width * self.__height)}'    
    
try:    
    h = float(input())
    w = float(input())
    r = Rectangle(w,h)
    print(r.user())
    print(r.area())
    print(r.perimeter())      
except ValueError:
    print("Wrong value")     