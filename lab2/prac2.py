from math import gcd

class Rational:	
    def __init__(self,numerator=1,denominator=1):
        if not isinstance(denominator,int) and isinstance(numerator,int):
            raise TypeError("Wrong type")
        if not denominator:
            raise ZeroDivisionError("Zero division error")
        newnumber = Rational.reducefraction(numerator,denominator)
        self.__numerator=newnumber[0]
        self.__denominator=newnumber[1]            
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
            raise TypeError
        denominator=int(self.__denominator*other.__denominator/gcd(self.__denominator,other.__denominator))
        numerator=int(denominator/self.__denominator*self.__numerator+denominator/other.__denominator*other.__numerator)
        k = Rational.reducefraction(int(numerator), int(denominator))      
        return Rational(k[0],k[1]) 
    
    def __sub__(self,other):
        if not isinstance(other,Rational):
            raise TypeError
        denominator=int(self.__denominator*other.__denominator/gcd(self.__denominator,other.__denominator))
        numerator=int(denominator/self.__denominator*self.__numerator-denominator/other.__denominator*other.__numerator) 
        k=Rational.reducefraction(int(numerator),int(denominator))       
        return Rational(k[0],k[1])
        
    def __mul__(self,other):
        if not isinstance(other,Rational):
            raise TypeError
        denominator=self.__denominator*other.__denominator
        numerator=self.__numerator*other.__numerator
        k=Rational.reducefraction(int(numerator),int(denominator))     
        return Rational(k[0],k[1])
    
    def __truediv__(self,other):
        if not isinstance(other,Rational):
            raise TypeError
        denominator=self.__denominator*other.__numerator
        numerator=self.__numerator*other.__denominator
        k=Rational.reducefraction(int(numerator),int(denominator))
        return Rational(k[0],k[1])
        
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

