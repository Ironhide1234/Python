
MAX_EMPLOYEES = 50
MAX_WORKEXP = 5

class Person:
    def __init__(self,surname,name,patronymic,birthdate):
        if not (isinstance(surname,str) and isinstance(name,str) and isinstance (patronymic,str) and isinstance(birthdate,str)):
            raise TypeError("Wrong type")
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birthdate = birthdate

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname
      
    @property
    def patronymic(self):
        return self.__patronymic
      
    @property 
    def birthdate(self):
        return self.__birthdate  

    @name.setter 
    def name(self,name):
        self.__name = name

    @surname.setter
    def surname(self,surname):
        self.__surname = surname    

    @birthdate.setter
    def birthdate(self,birthdate):
        self.__birthdate = birthdate        

    def __str__(self): 
        return f'Name:{self.__name}, Surname: {self.__surname}, Patronymic: {self.__patronymic},Birthdate:{self.__birthdate}'    


class Serviceman(Person):
    def __init__(self,name,surname,patronymic,birthdate,organisation,profession,salary,workexp,male):
        super().__init__(self,name,surname,patronymic,birthdate)
        self.organisation = organisation
        self.profession = profession
        self.salary = salary
        self.workexp = workexp
        self.male = male

    @property 
    def oranisation(self):
        return self.__organisation   

    @property 
    def profession(self):
        return self.__profession       

    @property 
    def salary(self):
        return self.__salary   

    @property
    def workexp(self):
        return self.__workexp

    @property
    def male(self):
        return self.__male    

    @organisation.setter
    def organisation(self,organisation):
        if not isinstance(organisation,int):   
            raise TypeError("Wrong type")
        self.__organisation = organisation     

    @profession.setter
    def profession(self,profession):
        if not isinstance(profession,int):
            raise TypeError("Wrong Type")
        self.__profession = profession     

    @salary.setter
    def salary(self,salary):
        if not isinstance(salary,int):
            raise TypeError("Wrong type")
        self.__salary = salary     
  
    @workexp.setter
    def workexp(self,workexp):
        if not isinstance(workexp,int):
            raise TypeError("Wrong type")
        self.__workexp = workexp

    @male.setter
    def male(self,male):
        if not isinstance(male,int):
            raise TypeError("Wrong type")
        self.__male = male
    
    def __str__(self): 
        return f'Name:{self.__name}\nSurname: {self.__surname}\nPatronymic: {self.__patronymic}\nBirthdate:{self.__birthdate}\nOrganisation:{self.__organisation}\n Profession:{self.__profession}\n Salary: {self.__salary}\n Working experience: {self.__workexp}\n Male: {self.__male}'    


class Organisation(Serviceman):

    member_list = []

    def __iter__(self):
        self.ind = -1
        return self

    def __next__(self):
        self.ind += 1
        if self.ind >= len(self.member_list):
            raise StopIteration
        return self.member_list[self.ind]


    def __init__(self,name,surname,patronymic,birthdate,organisation,profession,salary,workexp,male, *memb):
        if not all(isinstance(all_workers,Serviceman) for all_workers in memb):
            raise ValueError("Wrong value")
        super().__init__()
        
    def add(self,name,surname,patronymic,birthdate,organisation,profession,salary,workexp,male):
        for i in self.made_iterator:
            self.member_list.append(name,surname,patronymic,birthdate,organisation,profession,salary,workexp,male)


org = Organisation("aboba","")
    
    




 
