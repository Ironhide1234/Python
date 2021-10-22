class Stores:
    def __init__(self,name,price_serv,descr,prodim):
        if not (isinstance(price_serv,int) and isinstance(descr,str) and isinstance(prodim,str) and isinstance(name,str)): 
            raise TypeError("Wrong type")
        if not (name.isalpha() and price_serv > 0 and descr and prodim):
             raise ValueError("Wrong value") 
        self.__name = name
        self.price_serv = price_serv
        self.__descr = descr
        self.__prodim = prodim 

    def __str__(self):
        return f'Name:{self.__name}, Price: {self.price_serv}, Description: {self.__descr},Dimensions:{self.__prodim}'


class Customer:
    def __init__(self,Sur,Name,pat,mob):
        if not (isinstance(Name,str) and isinstance(Sur,str) and isinstance(pat,str) and isinstance(mob,str)):
            raise ValueError("Wrong value")
        if not (Name.isalpha() and Sur.isalpha() and pat.isalpha() and mob):
            raise TypeError("Wrong type") 
        self.__surname = Sur
        self.__name = Name
        self.__patronymic = pat
        self.__mobile = mob 

    def __str__(self):
            return f'Name: {self.__name}\nSur: {self.__surname}\nPat: {self.__patronymic}\nMobile: {self.__mobile}'


class Order:
    def __init__(self,cust, prod):
        if not (isinstance(cust,Customer) and all(isinstance(product,Stores) for product in prod)):
            raise TypeError("Wrong type")
        self.customer = cust
        self.prod = prod 

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




    
