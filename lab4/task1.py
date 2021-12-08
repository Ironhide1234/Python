from math import gcd

class Rational:	
    def __init__(self,numerator=1,denominator=1):
        self.numerator = numerator
        self.denominator = denominator 
        self.reducefraction()

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
 
    def reducefraction(self):
        k = gcd(self.__numerator,self.__denominator)
        if self.__denominator<0:
            self.__denominator=-self.__denominator
            self.__numerator=-self.__numerator
        self.__numerator //= k
        self.__denominator //= k
      
    def __str__(self):
        return f'{self.__numerator}/{self.__denominator}'
        
    def Showfloat(self):#lowercase
        return  float(self.__numerator/self.__denominator)
        
    def __add__(self,other):
        if not isinstance(other,Rational):
            raise TypeError("Wrong type")
        denominator=int(self.__denominator*other.__denominator/gcd(self.__denominator,other.__denominator))
        numerator=int(denominator/self.__denominator*self.__numerator+denominator/other.__denominator*other.__numerator)    
        return Rational(numerator,denominator)
    
    def __sub__(self,other):#intcheck
        if not isinstance(other,Rational):
            raise TypeError("Wrong type")
        denominator=int(self.__denominator*other.__denominator/gcd(self.__denominator,other.__denominator))
        numerator=int(denominator/self.__denominator*self.__numerator-denominator/other.__denominator*other.__numerator)       
        return Rational(numerator,denominator)
        
    def __mul__(self,other):
        if not isinstance(other,Rational):
            raise TypeError("Wrong type")
        denominator=self.__denominator*other.__denominator
        numerator=self.__numerator*other.__numerator
        return Rational(numerator,denominator)
    
    def __truediv__(self,other):
        if not isinstance(other,Rational):
            raise TypeError("Wrong type")
        denominator=self.__denominator*other.__numerator
        numerator=self.__numerator*other.__denominator
        return Rational(numerator,denominator)

    def __lt__(self,other):
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator
            
    def __gt__(self, other):
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator

    def __le__(self,other):
        self.__numerator * other.__denominator <= other.__numerator * self.__denominator 

    def __ge__(self, other):
        return self.__numerator * other.__denominator >= other.__numerator * self.__denominator  

    def __eq__(self, other):
        return self.__numerator * other.__denominator == other.__numerator * self.__denominator 

    def __ne__(self,other):
        return self.__numerator * other.__denominator != other.__numerator * self.__denominator 

    def __iadd__(self,other):      
        self.__numerator  = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        self.__denominator = self.__denominator*other.__denominator
        self.reducefraction()
        return self

    def __isub__(self,other):      
        self.__numerator  = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        self.__denominator = self.__denominator*other.__denominator
        self.reducefraction()
        return self
        


firstfraction=input()
secondfraction=input()
a=list(map(int,firstfraction.split('/')))
b=list(map(int,secondfraction.split('/')))
A=Rational(*a)
B=Rational(*b)
print(f'Form a/b(first): {A}')
print(f'Floatint-point format(first):  {A.Showfloat()}')
print(f'Form a/b(second): {B}')
print(f'Floatint-point format(second): {B.Showfloat()}')
C=A+B
print(f'A+B= {C}')
C=A*B
print(f'A*B= {C}')
C=A-B
print(f'A-B={C}')
C=A/B
print(f'A/B= {C}')
print(A!=B)
print(A==B)
C=A>B
print(C)
C=A<B
print(C)
A+=B
print(A)
A-=B
print(A)
print(A<=B)
































    # def __iadd__(self,other):
    #     denominator=int(self.__denominator*other.__denominator/gcd(self.__denominator,other.__denominator))
    #     numerator=int(denominator/self.__denominator*self.__numerator += denominator/other.__denominator*other.__numerator)
    #     k = Rational.reducefraction(int(numerator), int(denominator))
    #     return Rational(k[0],k[1])