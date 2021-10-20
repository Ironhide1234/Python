from math import gcd

class Rational:

	def __init__(self, num=1, denom=1):

		if isinstance(num, int) and isinstance(denom, int):#if int check
			if denom:
				self.__num = num
				self.__denom = denom	
			else:
				raise DivideByZero("Zero denom")
		else:
			raise TypeError("Error,wrong type")		


	def __str__(self):
		return f"({self.__num}, {self.__denom})"

	@staticmethod
	def reduce_fraction(n,m):#find highest comon divisor
	    k = gcd(n,m)
	    return (n//k, m//k)	


	def print_div(self):
		#rat type print
		return f'{self.__num}/{self.__denom}' if self.__num else "0"

	def  print_res_div(self):
		#show res of rat expr
		return f"{self.print_div()} = {round(self.__num/self.__denom,3)}"

	def __add__(self, other):
		
		if not  isinstance(other, Rational):
			raise TypeError("Rat type only")

		denom = int(self.__denom * other.__denom /  
					gcd ( self.__denom , other.__denom ))
		num = int(denom/self.__denom*self.__num + 
			denom/other.__denom*other.__num)
		res = Rational.reduce_fraction(int(num), int(denom))
		return Rational(res[0], res[1])	

	def __sub__(self, other):
		if not  isinstance(other, Rational):
			raise TypeError("Rat type only")

		denom = int(self.__denom * other.__denom /  
					gcd ( self.__denom , other.__denom ))
		num = int(denom/self.__denom*self.__num - 
			denom/other.__denom*other.__num) 
		result = Rational.reduce_fraction(int(num), int(denom))
		return Rational(result[0], result[1])	

	def __mul__(self, other):
		if not  isinstance(other, Rational):
			raise TypeError("Rat type only")
		denom = self.__denom * other.__denom
		num = self.__num * other.__num
		res = Rational.reduce_fraction(int(num), int(denom))
		return Rational(res[0], res[1])		


	def __truediv__(self, other):
		if not  isinstance(other, Rational):
			raise TypeError("sould be Rational type")
		denom = self.__denom * other.__num
		num = self.__num * other.__denom
		res = Rational.reduce_fraction(int(num), int(denom))
		return Rational(res[0], res[1])	



a = Rational()
assert a.print_div() == "1/1"		
assert a.print_res_div() == "1/1 = 1.0"
print(a, end="\n\n")

b = Rational(121, 11)
assert b.print_div() == "121/11"		
assert b.print_res_div() == "121/11 = 11.0"
print(b, end="\n\n")
a = Rational(3, 9)
b = Rational(3, 9)
c = a / b
assert c.print_div() == '1/1'

c = a * b
assert c.print_div() == '1/9'

c = a + b
assert c.print_div() == '2/3'
	
c = a - b
assert c.print_div() == '0'


