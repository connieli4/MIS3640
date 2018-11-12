from datetime import datetime

class People:

    def __init__(self, firstname, lastname, birthdate, favcolors = []):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.favcolors = []
        self.favcolors = favcolors
    
    def colors(self, color):
        self.favcolors().append(color)

    def age(self):
        today = datetime.today.year()
        age = today - self.birthdate.year
        return age
    
    
    def __str__(self):
        return '{} {} - favorite colors are: {}, age: {}'.format(self.firstname, self.lastname, self.favcolors, self.age)
    
    def __len__(self):
        return len(self.favcolors)


def main():
    person = People('John', 'Smith', datetime(2000, 12, 22), ['blue', 'green', 'yellow'])
    print(person)
    print(person.age)
    print(len(person))


if __name__ == '__main__':
    main()

