import re
import phonenumbers

class Stores:
    def __init__(self,name,price_serv,descr,prodim):
        self.name = name
        self.price_serv = price_serv
        self.descr = descr
        self.prodim = prodim 

    @property
    def name(self):
        return self.__name

    @property 
    def price_serv(self):    
        return self.__price_serv

    @property
    def descr(self):
        return self.__descr

    @property
    def prodim(self):
        return self.__prodim

    @staticmethod
    def __check_value(value):
        if not isinstance(value, str):
            raise TypeError("Wrong type of value")
        if not value:
            raise ValueError("Wrong Value")
        return True  
    
    @name.setter
    def name(self,value):
        if Stores.__check_value(value):
            self.__name = value

    @price_serv.setter    
    def price_serv(self,price_serv):
        if not isinstance(price_serv,int):
            raise TypeError("wrong type")
        self.__price_serv = price_serv  

    @descr.setter
    def descr(self,value):
        if  Stores.__check_value(value):
            self.__descr = value

    @prodim.setter
    def prodim(self,value):
        if  Stores.__check_value(value):
            self.__prodim = value
        
    def __str__(self): 
        return f'Name:{self.__name}, Price: {self.__price_serv}, Description: {self.__descr},Dimensions:{self.__prodim}'


class Customer:
    def __init__(self,Sur,Name,patronymic,mobile):
        self.surname = Sur
        self.name = Name
        self.patronymic = patronymic
        self.mobile = mobile 

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def mobile(self):
        return self.__mobile

    @staticmethod
    def __check_set_value(value):
        if not isinstance(value, str):
            raise TypeError("Wrong type of value")
        if not value:
            raise ValueError("Wrong Value")
        return True
    
    @name.setter
    def name(self,value):
        if Customer.__check_set_value(value):
            self.__name = value

    @surname.setter
    def surname(self,value):
        if Customer.__check_set_value(value):
            self.__surname = value

    @mobile.setter
    def mobile(self,value):
        flag = phonenumbers.parse(value)
        if not phonenumbers.is_possible_number(flag):
            raise ValueError("Wrong Value")
        self.__mobile = value 

    @patronymic.setter
    def patronymic(self,value):
        if Customer.__check_set_value(value):
            self.__patronymic = value

    def __str__(self):
        return f'Name: {self.name}\nSur: {self.surname}\nPat: {self.patronymic}\nMobile: {self.mobile}'


class Order:
    def __init__(self,cust, prod):
        if not (isinstance(cust,Customer) and all(isinstance(product,Stores) for product in prod)):
            raise TypeError("Wrong type")
        self.customer = cust
        self.prod = prod 

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self,customer):
        self.__customer = customer    

    def __str__(self):
        return f"Customer: {self.cust}\nProduct: {''.join(i for i in str(self.prod))}"

    def countval(self):
        cost = 0
        for product in self.prod:
            cost += product.price_serv
        return cost

    def addproduct(self,prod):
        if not( all(isinstance(product,Stores) for product in prod)): 
            raise TypeError("Wrong type")  
        self.prod +=list(prod)
        
    def deleteprod(self,prod):
        if  not (all(isinstance(product,Stores) for product in prod)):
            raise TypeError("Wrong type")
        for product in prod:
            self.prod.remove(product)          

    def infOrd(self):
        return self.prod

    def custinf(self):
        return self.customer             


arsen = Customer('Mets','Arsen', 'Anreevych', '+380989725758')
iPhone = Stores('Phone',8000,'phone', 'w: 7, l: 12')
Macbook = Stores('Laptop',24000, 'Note', 'w: 50, l: 70')
first = Order(arsen,[iPhone,Macbook])
print(first.custinf())
inform = list(first.infOrd())
for x in inform:
    print(x)
print(f'Your price is: {first.countval()}')




    
