from abc import ABC, abstractmethod

class ICourseFactory(ABC):
    @abstractmethod
    def setSpecialty():
        pass

class ICourse(ICourseFactory):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def setTeacher(self):
        pass

    @abstractmethod
    def setPlan(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class ITeacher(ICourseFactory):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def setName(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ILocalCourse(ICourse):
  @abstractmethod
  def setAuditory(self):
    pass


class IOffsiteCourse(ICourse):
  @abstractmethod
  def setPlace(self):
    pass
