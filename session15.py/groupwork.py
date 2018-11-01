from datetime import datetime

class People:

    def __init__(self, firstname, lastname, birthdate):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age
    
    def __str__(self):
        return '{}{},{}'.format(self.firstname, self.lastname, self.age)


person = People('John', 'Smith', 2000)

print(person)