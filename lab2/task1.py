class Stores:
    def __init__(self,name,price_serv,descr,prodim):
        if isinstance(price_serv,int) and isinstance(descr,str) and isinstance(prodim,str) and isinstance(name,str): 
            if name.isalpha() and price_serv > 0 and descr and prodim:
                self.__name = name
                self.price_serv = price_serv
                self.__descr = descr
                self.__prodim = prodim 
            else:
                raise ValueError("Wrong value")  
        else:
            raise TypeError("Wrong type")            
    def __str__(self):
        return f'Name:{self.__name}, Price: {self.price_serv}, Description: {self.__descr},Dimensions:{self.__prodim}'

class Customer:
    def __init__(self,Sur,Name,pat,mob):
        if isinstance(Name,str) and isinstance(Sur,str) and isinstance(pat,str) and isinstance(mob,str):
            if Name.isalpha() and Sur.isalpha() and pat.isalpha() and mob:
                self.__surname = Sur
                self.__name = Name
                self.__patronymic = pat
                self.__mobile = mob  
            else:
                raise ValueError("Wrong value")   
        else:
            raise TypeError("Wrong type")             
    def __str__(self):
            return f'Name: {self.__name}\nSur: {self.__surname}'

class Order:
    def __init__(self,cust, prod):
        if isinstance(cust,Customer) and all(isinstance(product,Stores) for product in prod):
            self.customer = cust
            self.prod = prod
        else:
            raise TypeError("Wrong type")   
    def countval(self):
        cost = 0
        for product in self.prod:
            cost += product.price_serv
        return f'Total price: {cost}'    
    def addproduct(self,prod):
        if all(isinstance(product,Stores) for product in prod):  
            self.prod +=list(prod)
        else:
            raise TypeError("Wrong type") 
    def deleteprod(self,prod):
        if all(isinstance(product,Stores) for product in prod):
            for product in prod:
                self.prod.remove(product)          
        else:
            raise TypeError("Wrong type") 
    def info(self):
        return self.prod
    def custinf(self):
        return self.customer             





arsen = Customer('Mets','Arsen', 'Anreevych', '+380989725758')
iPhone = Stores('Phone',8000,'phone', 'w: 7, l: 12')
Macbook = Stores('Laptop',24000, 'Note', 'w: 50, l: 70')
first = Order(arsen,[iPhone,Macbook])
print(first.custinf())
inform = list(first.info())
for x in inform:
    print(x)
print(first.countval())




    
