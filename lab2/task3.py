from operator import methodcaller

class Student:
    
    def __init__(self,name,surname,booknumb,grade):
        if not (isinstance(name,str) and isinstance(surname,str) and isinstance(booknumb,int) and isinstance(grade,list)):
            raise ValueError("Wrong value")  
        if not (name.isalpha() and surname.isalpha() and booknumb > 0):
            raise TypeError("Wrong type") 
        self.booknumb  = booknumb
        self.surname = surname
        self.name = name
        self.grade = grade

    def find_grade(self): 
        return sum(self.grade)/len(self.grade)
        
    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @staticmethod
    def __check_set_value(value):
        if not isinstance(value, str):
            raise TypeError("Wrong type of value")
        if not value:
            raise ValueError("Wrong Value")
        return True

    @name.setter
    def name(self, value):
        if Student.__check_set_value(value):
            self.__name = value

    @surname.setter
    def surname(self, value):
        if Student.__check_set_value(value):
            self.__surname = value

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        if not isinstance(grade, list):
            raise TypeError("Wrong type of grade")
        self.__grade = grade

    def __str__(self):
        return f'Name: {self.name}, Record book number: {self.booknumb}, Surname: {self.surname}, Grade: {self.find_grade()}'

MAX_STUDENTS = 20


class Group:
    
    surname_name = []

    def __init__(self, *stud):
        if not all(isinstance(student,Student) for student in stud):
            raise ValueError("Wrong value")
        if not len(stud)<=MAX_STUDENTS:
            raise TypeError("Wrong type")
        for student in stud:
            if f'{student.name} {student.surname}' in Group.surname_name:
                raise ValueError("Same name")
            for grade in student.grade:
                if not isinstance(grade,int):
                    raise TypeError("Wrong type")
                if not (1 <= grade <= 5):   
                    raise ValueError("Incorrect value")
            Group.surname_name.append(f'{student.name} {student.surname}')    
        self.stud = stud   

    def hscore(self):
        hs = sorted(self.stud,key = methodcaller('find_grade'),reverse = True)
        return hs[:5]        


one=Student("Itachenko","Sharingan",5,[5,5,5])
two=Student("Uzumaki","Naruto",1,[4,4,4])
three=Student("Marmeladova","Sonya",5,[4,3,2])
four=Student("Vodoleev","Illya",3,[2,3,4])
five=Student("Mets","Arseniy",7,[2,3,4])
six=Student("Kolotushkin","Pushkin",7,[2,4,1])
seven=Student("Sievertsev","Kolya",10,[2,2,5])
eight=Student("Lagoida","Misha",9,[2,2,2])
nine=Student("Popov","Evgeniy",8,[3,4,5])
ten=Student("Pavlyuk","Vasya",6,[3,3,3])
ti_01=Group(one,two,three,four,five,six,seven,eight,nine,ten)
for student in ti_01.hscore():
    print(student)