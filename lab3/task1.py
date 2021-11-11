import sys
import json
import datetime
import os
import time


class RegularTicket:
    def __init__(self,price,event,user_data,date_of_event):
        self.id = self.generate_id()
        self.price = price
        self.user_data = user_data
        self.event = event
        self.date_of_event = date_of_event

    def load_ticket(self):
        file = open(self.id + '.json', 'w')
        json.dump(self.__dict__,file, indent = 2)
        file.close()

    def get_info_ticket(filename):
        if not os.path.exists(filename + '.json'):
            raise FileNotFoundError
        file = open(filename + '.json', "r")    
        info = json.load(file)
        user_data = input['user_data']
        price = input['price']
        event = input['event']
        date_of_event = input['date_of_event']
        file.close()
        return f'Your info:\nUser:{user_data}\nPrice:{round(price)}\nEvent:{event}Event date:{date_of_event}'
    
    def create_ticket(filename):
        if not os.path.exists(filename):
            raise FileNotFoundError
        file = open(filename, "r")
        input = json.load(file)
        user_data = input['user_data']
        main_price = input['main_price']
        event = input['event']
        date_of_event = input['date_of_event']
        student = True
        if 'student' in input:
            student = input['student']
        file.close()
        return RegularTicket.genTicket(user_data,event,main_price,date_of_event,student)    

    def genTicket(user_data,event,main_price,date_of_event,student = True):
        if not(isinstance(date_of_event,str) and isinstance(main_price,int) and isinstance(user_data,str) and isinstance(student,bool) and isinstance(event,str)):
            raise TypeError("Wrong type")
        if student == True:
            return StudentTicket(user_data,event,date_of_event,main_price)
        elif RegularTicket.daysToEvent(date_of_event) > 60:
            return AdvancedTicket(user_data,event,date_of_event,main_price)        
        else:
            return LateTicket(user_data,event,date_of_event,main_price)

    def generate_id(self):
        currentTime = datetime.now()
        year = currentTime.year
        month = currentTime.month
        day = currentTime.day
        hour = currentTime.hour
        minute = currentTime.minute
        sec = currentTime.second
        mcsec = currentTime.microsecond
        time.sleep(0.001)
        return f"{year}-{month}-{day}-{hour}-{minute}-{sec}-{mcsec}"     

    def daysToEvent(date_of_event):
        try:
            d1 = datetime.now()
            d2 = datetime.strptime(date_of_event,"%d.%m.%Y") 
        except:
            raise ValueError("Wrong type of date")
        days = (d2 - d1).days
        if days < 0:
            raise ValueError("Wrong date")
        else:
            return days  

    def __str__(self):
        return f"{self.id}\n{self.user_data}\nevent: {self.event}\ntotal price: {round(self.price)}"            

class AdvancedTicket(RegularTicket):
    def __init__(self,user_data,price,date_of_event,event):
        super().__init__(user_data,event,price * 0.6,date_of_event)


class LateTicket(RegularTicket):
    def __init__(self, user_data, event, price, date_of_event):
        super().__init__(user_data, event, price * 1.1, date_of_event)


class StudentTicket(RegularTicket):
    def __init__(self,user_data,price,date_of_event,event):
        super().__init__(user_data,event,price * 0.5,date_of_event)       

print(RegularTicket.create_ticket("data.json"))         
