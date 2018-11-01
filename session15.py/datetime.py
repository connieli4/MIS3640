from datetime import datetime


def days_until_birthday(birthday):
    """How long until my next birthday?"""
    today = datetime.today()
    next_birthday = datetime(today.year, birthday.month, birthday.day)
    if next_birthday <= today:
        next_birthday = datetime(today.year, birthday.month, birthday.day)
    delta = next_birthday - today
    return delta.days


def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.
    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """
    b1 = datetime()
    b2 = datetime()
    age_b1 = 2018 - datetime(b1.year)
    age_b2 = 2018 - datetime(b2.year)
    if (age_b1 == age_b2 * 2):
        print(datetime(b1.day))
    elif (age_b2 == age_b1 * 2):
        print(datetime(b2.day))
    else:
        print('The person is not twice as old')


def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week
    today = datetime.today()
    print(today.weekday())

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = datetime(1997, 10, 25)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = datetime(2017, 12, 25)
    b2 = datetime(2010, 11, 1)
    print('Double Day', end=' ')
    print(double_day(b1, b2))


# def main():
#     datetime_exercises()


if __name__ == '__main__':
    datetime_exercises()