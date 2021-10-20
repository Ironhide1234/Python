from operator import methodcaller

class Student:
    surname_name = []
    def __init__(self,name,surname,booknumb,grade):
        if isinstance(name,str) and isinstance(surname,str) and isinstance(booknumb,int) and isinstance(grade,list):
            if name.isalpha() and surname.isalpha() and booknumb > 0 and all(0<=grades<=100 for grades in grade) and not f'{surname} {name}' in Student.surname_name:
                Student.surname_name.append(f'{surname} {name}')
                self.name = name
                self.surname = surname
                self.booknumb  = booknumb
                self.grade = list(grade)
            else:
                raise TypeError("Wrong type") 
        else:
            raise ValueError("Wrong value")    
    def avggr(self): 
        return sum(self.grade)/len(self.grade)
    def __str__(self):
        return f'Name: {self.name}, Record book number: {self.booknumb}, Surname: {self.surname}'


class Group:
    def __init__(self, *stud):
        if all(isinstance(student,Student) for student in stud):
            if len(stud)<=20:
                self.stud = stud
            else:
                raise ValueError("Wrong value")
        else:
            raise TypeError("Wrong type")
    def hscore(self):
        hs = sorted(self.stud,key = methodcaller('avggr'),reverse = True)
        return hs[:10]        


one=Student("Sharingan","Itachenko",5,[6,6,6])
two=Student("Naruto","Uzumaki",1,[4,4,4])
three=Student("Silpo","Marmeladov",5,[4,3,2])
four=Student("Illya","Vodoleev",3,[2,3,4])
five=Student("Arseniy","Mets",5,[2,3,4])
six=Student("Pushkin","Kolotushkin",7,[2,4,1])
seven=Student("Kolya","Sievertsev",10,[2,2,5])
eight=Student("Misha","Lagoida",9,[2,2,2])
nine=Student("Evgeniy","Popov",3,[3,4,5])
ten=Student("Vasya","Pavlyuk",6,[3,2,1])
ti_01=Group(one,two,three,four,five,six,seven,eight,nine,ten)
for student in ti_01.hscore():
    print(student)