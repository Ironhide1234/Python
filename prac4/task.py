# def add_field(cls):
#     def adder(*args,**kwargs):
#         new_instance = cls(*args,**kwargs)
#         new_instance = AnotherClass()
#         new_instance.new_field = ''
#         new_instance.count = 1
#         return new_instance

#     return adder    

# class AnotherClass:
#     def __init__(self):
#         print('another class created')

# @add_field
# class Student:
#     def __init__(self,name,surname):
#         self.name = name
#         self.surname = surname

#     def __str__(self):
#         return f'{self.name} {self.surname}'

# def main():
#     x = Student('Petr','Petrov')  

# if __name__ == '__main__':
#     main()       


class Sequance:
    def __init__(self,start,stop,step):
        self.start = start
        self.stop = stop
        self.step = step
        self.count = 0

    def __call__(self, *args,**kwargs):
        self.count += 1
        curr = self.start + self.count * self.step
        if curr <= self.stop:
            return curr
        return None

x = Sequance(1,20,3)
print(x())                