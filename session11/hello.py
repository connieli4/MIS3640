
def replace_even(data):
    for i in range(0,len(data),2):
        data[i] = 0
    return(data)
    

# Uncomment the following lines to test
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
replace_even(ONE_TEN)
print(ONE_TEN)

# Expected output:
# [0, 2, 0, 4, 0, 6, 0, 8, 0, 10]

def remove_middle(data):
    if len(data)%2==0:
        del data[int(len(data)/2)]
        del data[int(len(data)/2)]
    else:
        del data[int(len(data)/2)]
    return data
    

# Uncomment the following lines to test
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
remove_middle(ONE_TEN)
print(ONE_TEN)

# Expected output:
# [1, 2, 3, 4, 7, 8, 9, 10]

def insert_integer(data, number):
   for n in range(0, len(data)):
       if (data[n] >= number):
           data.insert(n, number)
           break
   return data    


data = [1, 3, 40, 75, 90, 2000, 2001, 2016]

new_data = insert_integer(data, 2015)

print(new_data)

# Expected output:
# [1, 3, 40, 75, 90, 2000, 2001, 2015, 2016]

def print_hist(data):
    for item in sorted(data):
        print(item,'*'*data[item])

letter_counts={'C': 6, 'A': 3, 'B': 10, 'Z': 8}
print_hist(letter_counts)
'''
    Expected output:
    A: ***
    B: **********
    C: ******
    Z: ********
""" 

import random

class_roster = {'Jonathan Beltran': 0, 'Allison Fernandez': 1, 'Siddhanth Goyal': 0, 'Jingyu He': 0, 'Defne Ikiz': 0, 'Zirui Jiao': 0, 'Pranjal Joshi': 0, 'Dong Hyun Kim': 0, 'Ha Min Ko': 0, 'Kyle Lawson': 0, 'Christine Lee': 1, 'Connie Li': 1,
               'Qinyi Li': 0, 'Matthew Michalke': 0, 'Ho Wang Alastair Ng': 1, 'Jonghyun Park': 0, 'Alden Pexton': 2, 'Shriya Rathi': 2, 'Waylon Ryan': 1, 'Christian Thompson': 3, 'Angela Tsung': 2, 'Aaron Wendell': 0, 'Sarah Zazyczny': 0, 'Shiyue (Shirley) Zong': 0}