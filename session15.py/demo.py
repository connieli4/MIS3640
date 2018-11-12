class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time():
    print('The current time is {}:{}:{}.'.format(time.hour, time.minute, time.second))

print_time()

def is_after(t1, t2):
    if t1.hour > t2.hour:
        return True
    elif t1.hour == t2.hour:
        if t1.minute > t2.minute:
            return True
        elif t1.minute == t2.minute:
            return t1.second > t2.second
        else:
            return False
    else:
        return False

time2 = Time()
time2.hour = 1
time2.minute = 12
time2.second = 14

print(is_after(time, time2))

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum

start = Time()
start.hour = 9
start.minute = 45
start.second =  0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start, duration)
print_time(done)

def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def increment_2(time, seconds):
    result = Time()
    result.hour, result.minute, result.second = time.hour, time.minute, time.second
    if result.second >= 60:
        result.second -= 60
        result.minute += 1
    if result.minute >= 60:
        result.minute -= 60
        result.hour += 1
    return result

def sub_time(t1, t2):
    seconds = time_to_int(t1) - time_to_int(t2)
    return int_to_time(seconds)

def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


def add_time_2(t1, t2):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time, stupid!')
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

done = add_time(start, duration)
print_time(done)
another = add_time2(done, duration)
print(another)

def mul_time(t1, num):
    if not valid_time(t1) or not valid_time(t2):
        raise ValueError('invalid Time object in add_time, stupid!')
    seconds = time_to_int(t1) * num
    return int_to_time(seconds)