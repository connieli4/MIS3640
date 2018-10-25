# def sum_list(t):
#     if type(t) != list:
#         return t
#     if t == []:
#         return 0
#     return sum_list(t[0]) + sum_list(t[1:])

# print(sum_list([[1, 2], [3], [4, 5, 6]]))


# def cumsum(t):
#     total = 0
#     new_list = []
#     for x in t:
#         total += x
#         new_list.append(total)
#     return cumsum


# t = [1, 2, 3, 4, 5, 5]

# def middle(t):
#     return t[1:-1]
    
# print(middle(t))

# def chop(t):
#     del t[0]
#     del t[-1]
#     return t

# print(chop(t))

# def is_sorted(t):
#     return t == sorted(t)


# is_sorted(t)
# is_sorted(['2', '1', '3', '2'])

# def is_anagram(x, y):
#     return sorted(x) == sorted(y)
   

# is_anagram('star', 'rats')

# def has_duplicates(s):
#     for x in s:
#         if s.count(x) > 1:
#             return True
#     return False

# has_duplicates('cbba')
# has_duplicates('cba')

# def has_adjacent_duplicates(s):
#     """Returns True if there are two same adjacent elements.
#     s: string or list
#     returns: bool
#     output:
#     >>> print(has_adjacent_duplicates('cba'))
#     False
#     >>> print(has_adjacent_duplicates('abca'))
#     Flase
#     >>> print(has_adjacent_duplicates('abbc'))
#     True
#     """
#     for i in range(len(s)-1):
#         if s[i] == s[i+1]:
#             return True
#     return False


# def main():
#     t = [[1, 2], [3], [4, 5, 6]]
#     print(nested_sum(t))

#     t = [1, 2, 3]
#     print(cumsum(t))

#     t = [1, 2, 3, 4]
#     print(middle(t))
#     chop(t)
#     print(t)

#     print(is_sorted([1, 2, 2]))
#     print(is_sorted(['b', 'a']))

#     print(is_anagram('stop', 'pots'))
#     print(is_anagram('different', 'letters'))
#     print(is_anagram([1, 2, 2], [2, 1, 2]))

#     print(has_duplicates('cba'))
#     print(has_duplicates('abba'))


# if __name__ == '__main__':
#     main()

def oddNumbers(l, r):
    arr = []
    for number in range(l, r+1):
        if (number % 2) >= 1:
            arr.append(number)
    return arr

# print(oddNumbers(3, 9))


import random
import pprint

class_roster = {'Jonathan Beltran': 0, 'Allison Fernandez': 1, 'Siddhanth Goyal': 0, 'Jingyu He': 0, 'Defne Ikiz': 0, 'Zirui Jiao': 0, 'Pranjal Joshi': 0, 'Dong Hyun Kim': 0, 'Ha Min Ko': 0, 'Kyle Lawson': 0, 'Christine Lee': 1, 'Connie Li': 1,
               'Qinyi Li': 0, 'Matthew Michalke': 0, 'Ho Wang Alastair Ng': 1, 'Jonghyun Park': 0, 'Alden Pexton': 2, 'Shriya Rathi': 2, 'Waylon Ryan': 1, 'Christian Thompson': 3, 'Angela Tsung': 2, 'Aaron Wendell': 0, 'Sarah Zazyczny': 0, 'Shiyue (Shirley) Zong': 0}

pprint.pprint(class_roster)
min_times = min(class_roster.values())
pool = []

for names in class_roster:
    if class_roster[names] == min_times:
        pool.append(names)
        class_roster[names] += 1

random_name = random.choice(pool)
print(random_name)
print(class_roster)
