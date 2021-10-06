class Stores:
    def __init__(self,price_serv,descr,prodim):
        self.__price_serv = price_serv
        self.__descr = descr
        self.__prodim = prodim 
    def get_price(self):
        return self.__price_serv

class Customer:
       def __init__(self,Sur,Name,pat,mob):
           self.__surname = Sur
           self.__name = Name
           self.__patronymic = pat
           self.__mobile = mob  
       def __str__(self):
            return f'Name: {self.__name}\nSur: {self.__surname}'

class Order:
    def __init__(self,cust,prod):
        self.__customer = cust
        self.__product = prod
        self.__price = self.orderpr()
    def orderpr(self):
        cost = 0
        for i in range(len(self.__product)):
            cost += self.__product[i].get_price()
        return cost
    def __str__(self):
        return f'{self.__customer}\ntotal price: {self.__price}'        

try:
    arsen = Customer('Arsen', 'Mets', 'Anreevych', '+380989725758')
    iPhone = Stores(8000, 'Phone', 'w: 7, l: 12')
    Macbook = Stores(24000, 'Laptop', 'w: 50, l: 70')
    mainOrder = Order(arsen, [iPhone, Macbook])
    print(mainOrder)
except:
    print('Oops,sth broken down!')





    
