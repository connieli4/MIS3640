from BabsonPerson import BabsonPerson
from Person import Person


class Professor(BabsonPerson):
    def __init__(self, name, department, yrs_Babson, age):
        BabsonPerson.__init__(self, name)
        self.name = name
        self.department = department
        self.yrs_Babson = yrs_Babson
        self.age = age

