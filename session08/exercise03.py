# string = "  -Babson College is on the East Coast-   "
# print(string.split())
# print(string.strip(' -'))
# print(string.replace('a', 'o', 2))

string = "absdefghijklmnopqrstuvwxyz"

my_sum = 0
def calc_dol(s, letter):
    for i in s:
        my_sum += [i] + 1
    return my_sum

calc_dol(1, 'a')