class Queue:

    user_data = []

    def __init__(self,queuenum,surname,famcons,name,data):
        if not (isinstance(name,str) and isinstance(surname,str) and isinstance(queuenum,int) and isinstance(famcons,list) and isinstance(data,str)): 
            raise TypeError("Wrong type")
        if not (surname.isalpha() and queuenum > 0 and famcons and name.isalpha()):
             raise ValueError("Wrong value") 
        self.queuenum =queuenum
        self.surname = surname
        self.famcons = famcons
        self.name = name 
        self.data = data

    @property
    def surname(self):
        return self.__surname

    @property 
    def queuenum(self):    
        return self.__queuenum

    @property
    def famcons(self):
        return self.__famcons

    @property
    def name(self):
        return self.__name

    @staticmethod
    def __check_value(value):
        if not isinstance(value, str):
            raise TypeError("Wrong type of value")
        if not value:
            raise ValueError("Wrong Value")
        return True  
    
    @surname.setter
    def surname(self,value):
        if Queue.__check_value(value):
            self.__surname = value

    @queuenum.setter    
    def price_serv(self,queuenum):
        if not isinstance(queuenum,int):
            raise TypeError("wrong type")
        self.__queuenum = queuenum  

    @famcons.setter
    def descr(self,famcons):
        if not isinstance(famcons, list):
            raise TypeError("Wrong type of family consistance")
        self.__famcons = famcons

    @name.setter
    def name(self,value):
        if Queue.__check_value(value):
            self.__name = value

    def __str__(self): 
        return f'Name: {self.__name}, Surname:{self.__surname}, Queuenum: {self.__queuenum}, Family: {self.__famcons},Data:{self.__data}'
  
    def add_user(self, *allus):
        if not all(isinstance(users,Queue) for users in allus):
            raise ValueError("Wrong value")
        for users in allus:
            if f'{users.name} {users.surname}' in Queue.user_data:
                raise ValueError("Same name")
        Queue.user_data.apppend(f'{users.name} {users.surname} {users.queuenum} {users.famcons} {users.data}')  

    def delete_user(self, *allus,delitem):
        if not all(isinstance(users,Queue) for users in allus):
            raise ValueError("Wrong value")
        for users in allus:
            if f'{users.name} {users.surname}' in Queue.user_data:
                raise ValueError("Same name")
        Queue.user_data.pop([delitem])

    def search_user(self, *allus,search_item):
            if not all(isinstance(users,Queue) for users in allus):
                raise ValueError("Wrong value")
            for users in allus:
                if f'{users.name} {users.surname}' in Queue.user_data:
                    raise ValueError("Same name")
            return Queue.user_data.index([search_item])  
            
one=Queue("Itachenko","Sharingan",3,"Pasha","30.10.2010")
two=Queue("Uzumaki","Naruto",1,"Sasha ","31.12.2012")
three=Queue("Marmeladova","Sonya",5,"Masha","12.10.2008")    

print(one)
