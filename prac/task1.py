class Rectangle:
    def __init__(self,width = 1, height = 1):
        self.setter(width,height)
    def setter(self,width,height):
        if  h < 0 and w < 0 or h >= 20 and w >= 20:
            print("Incorrect number")
        else:
            self.height  = height      
            self.width = width
    def perimeter(self):
        return 2 * self.height + 2 * self.width
    def area(self):
        return self.width * self.height 
    def getStats(self):
        return "width:  %s\nheight:     %s\narea:      %s\nperimeter: %s" % (self.width, self.height, self.area(), self.perimeter())
    
    
try:    
    h = float(input())
    w = float(input())
    r = Rectangle(w,h)
    print(r.getStats())      
except:
    print("Error1")        