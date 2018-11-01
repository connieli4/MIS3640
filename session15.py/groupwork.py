from datetime import datetime

class People:

    def __init__(self, firstname, lastname, birthdate):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate

    def age(self):
        today = datetime.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return age
    
    def __str__(self):
        return '{} {},{}'.format(self.firstname, self.lastname, self.age)


def main():
    person = People('John', 'Smith', datetime(2000, 12, 22))
    print(person)


if __name__ == '__main__':
    main()

