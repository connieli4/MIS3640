#date_fashion
def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    return 1

#squirrel_play
def squirrel_play(temp, is_summer):
    if is_summer:
        return 60 <= temp <= 100
    return 60 <= temp <= 90

#caught_speeding
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return 0
    if 60 < speed <= 80:
        return 1
    return 2


#sorta_sum
def sorta_sum(a, b):
    if 10 <= a + b < 20:
        return 20
    return a + b

#alarm_clock
def alarm_clock(day, vacation):
    if not vacation:
        if 1 <= day <= 5:
            return '7:00'
        return '10:00'
    if 1 <= day <= 5:
        return '10:00'
    return 'off'

#love6
def love6(a, b):
    return 6 in [a, b, a + b, abs(a - b)]

#in1to10
def in1to10(n, outside_mode):
    if not outside_mode:
        return n in range(1, 11)
    return n <= 1 or n >= 10

#near_ten
def near_ten(num):
     # return 0 <= (num % 10) <= 2 or 8 <= (num % 10) <= 10
    return num % 10 in [0,1,2,8,9,10]
