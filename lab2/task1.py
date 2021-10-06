class Stores:
    def __init__(self,price_serv,order_price,descr,prodim):
        self.price_serv = price_serv
        self.descr = descr
        self.prodim = prodim 
        self.order_price = order_price
    def store_info(self):
        return self.descr,self.prodim,self.order_price,self.price_serv

class Customer:
       def __init__(self,surname,name,patronymic,mob):
           self.surname = surname
           self.name = name
           self.patronymic = patronymic
           self.mob = mob  
        def cust_info(self):
            return self.name,self.surname,self.patronymic,self.mob

class Order(Stores,Customer):
    def __init__(self,order_name,order_val):
        self.order_val = order_val
        self.order_name = order_name








    
