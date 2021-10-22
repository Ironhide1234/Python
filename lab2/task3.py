from operator import methodcaller

class Student:
    
    def __init__(self,name,surname,booknumb,grade):
        if not (isinstance(name,str) and isinstance(surname,str) and isinstance(booknumb,int) and isinstance(grade,list)):
            raise ValueError("Wrong value")  
        if not (name.isalpha() and surname.isalpha() and booknumb > 0 and all(0<=grades<=100 for grades in grade)):
            raise TypeError("Wrong type") 
        self.booknumb  = booknumb
        self.surname = surname
        self.name = name
        self.grade = list(grade)

    def find_grade(self): 
        return sum(self.grade)/len(self.grade)

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
            Group.surname_name.append(f'{student.name} {student.surname}')    
        self.stud = stud   

    def hscore(self):
        hs = sorted(self.stud,key = methodcaller('find_grade'),reverse = True)
        return hs[:5]        


one=Student("Itachenko","Sharingan",5,[6,6,6])
two=Student("Uzumaki","Naruto",1,[4,4,4])
three=Student("Marmeladov","Silpo",5,[4,3,2])
four=Student("Vodoleev","Illya",3,[2,3,4])
five=Student("Mets","Arseniy",7,[2,3,4])
six=Student("Kolotushkin","Pushkin",7,[2,4,1])
seven=Student("Sievertsev","Kolya",10,[2,2,5])
eight=Student("Lagoida","Misha",9,[2,2,2])
nine=Student("Popov","Evgeniy",8,[3,4,5])
ten=Student("Pavlyuk","Vasya",6,[3,2,1])
ti_01=Group(one,two,three,four,five,six,seven,eight,nine,ten)
for student in ti_01.hscore():
    print(student)