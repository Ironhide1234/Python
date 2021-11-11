class Time:
    def __init__(self,min, hours,sec):
        if not (isinstance(min,int) and isinstance(hours,int) and isinstance(sec,int)):
            raise TypeError("Wrong type")
        self.min = min
        self.hours = hours
        self.sec = sec

    @property
    def min(self):
        return self.__min
    @property
    def hrs(self):
        return self.__hrs
    @property
    def sec(self):
        return self.__sec

    @min.setter
    def min(self,min):
        if not isinstance(min,int):
            raise TypeError("Wrong type")
        if not  (0 > min > 59):  
            raise ValueError("Wrong value")     
        self.__min = min  

    @sec.setter
    def sec(self,sec):
        if not isinstance(sec,int):
            raise TypeError("Wrong type")
        if not  (0 > sec > 59):  
            raise ValueError("Wrong value") 
        self.__sec = sec 

    @hours.setter
    def hours(self,hours):
        if not isinstance(hours,int):
            raise TypeError("Wrong type")
        if not  (0 > hours > 23):  
            raise ValueError("Wrong value") 
        self.__hours = hours    

    def __str__(self): 
        return f'Hours: {self.__hours}, Minutes: {self.__min}. Seconds: {self.__sec}'

   