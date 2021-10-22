class Rectangle:
    def __init__(self,width = 1, height = 1):
        self.__height  = height      
        self.__width = width
    @staticmethod
    def check(value):
        if not isinstance(value,float):
            raise TypeError("Wrong type")
        if not (value <= 20 and value > 0):
            raise ValueError("Wrong value")
        return True    
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height    
    @height.setter
    def height(self,height):
        if Rectangle.check(height):
            self.__height = height           
    @width.setter
    def width(self,width):
        if  Rectangle.check(width):
            self.__width = width           
    def calcPer(self):
        return (self.__width + self.__height) * 2
    def calcAr(self):
        return self.__width * self.__height    
       
h = float(input())
w = float(input())
r = Rectangle(w,h)
print(f'Your height:{r.height}  Your width:{r.width}')
print(f'Your area: {r.calcAr()}')
print(f'Your perimeter: {r.calcPer()}')      
 