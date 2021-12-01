from math import gcd

class Rational:	
    def __init__(self,numerator=1,denominator=1):
        newnumber = Rational.reducefraction(numerator,denominator)
        self.numerator=newnumber[0]
        self.denominator=newnumber[1]   

    @property
    def numerator(self):     
        return self.__numerator   

    @property
    def denominator(self):     
        return self.__denominator    

    @numerator.setter
    def numerator(self,numerator):
        if not isinstance(numerator,int):
            raise TypeError("Wrong type")
        self.__numerator = numerator   

    @denominator.setter
    def denominator(self,denominator):
        if not isinstance(denominator,int):
            raise TypeError("Wrong type")
        if not denominator:
            raise ZeroDivisionError("Zero division error")
        self.__denominator = denominator    

    @staticmethod  
    def reducefraction(x,y):
        k = gcd(x,y)
        if y<0:
            y=-y
            x=-x
        return (x//k, y//k)
      
    def ShowFraction(self):
        return f'{self.__numerator}/{self.__denominator}'
        
    def Showfloat(self):
        return  float(self.__numerator/self.__denominator)
        
    def __add__(self,other):
        if not isinstance(other,Rational):
            raise TypeError("Wrong type")
        denominator=int(self.__denominator*other.__denominator/gcd(self.__denominator,other.__denominator))
        numerator=int(denominator/self.__denominator*self.__numerator+denominator/other.__denominator*other.__numerator)
        k = Rational.reducefraction(int(numerator), int(denominator))      
        return Rational(k[0],k[1]) 
    
    def __sub__(self,other):
        if not isinstance(other,Rational):
            raise TypeError("Wrong type")
        denominator=int(self.__denominator*other.__denominator/gcd(self.__denominator,other.__denominator))
        numerator=int(denominator/self.__denominator*self.__numerator-denominator/other.__denominator*other.__numerator) 
        k=Rational.reducefraction(int(numerator),int(denominator))       
        return Rational(k[0],k[1])
        
    def __mul__(self,other):
        if not isinstance(other,Rational):
            raise TypeError("Wrong type")
        denominator=self.__denominator*other.__denominator
        numerator=self.__numerator*other.__numerator
        k=Rational.reducefraction(int(numerator),int(denominator))     
        return Rational(k[0],k[1])
    
    def __truediv__(self,other):
        if not isinstance(other,Rational):
            raise TypeError("Wrong type")
        denominator=self.__denominator*other.__numerator
        numerator=self.__numerator*other.__denominator
        k=Rational.reducefraction(int(numerator),int(denominator))
        return Rational(k[0],k[1])

    def __lt__(self,other):
        if self.__numerator/self.__denominator < other.__numerator/other.__denominator:
            return f'B number is bigger'
        else:
            return f'A number is bigger'

firstfraction=input()
secondfraction=input()
a=list(map(int,firstfraction.split('/')))
b=list(map(int,secondfraction.split('/')))
A=Rational(a[0],a[1])
B=Rational(b[0],b[1])
print(f'Form a/b(first): {A.ShowFraction()}')
print(f'Floatint-point format(first):  {A.Showfloat()}')
print(f'Form a/b(second): {B.ShowFraction()}')
print(f'Floatint-point format(second): {B.Showfloat()}')
C=A+B
print(f'A+B= {C.ShowFraction()}')
C=A*B
print(f'A*B= {C.ShowFraction()}')
C=A-B
print(f'A-B={C.ShowFraction()}')
C=A/B
print(f'A/B= {C.ShowFraction()}')
print(A<B)
