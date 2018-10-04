def sum_list(t):
    if type(t) != list:
        return t
    if t == []:
        return 0
    return sum_list(t[0]) + sum_list(t[1:])

print(sum_list([[1, 2], [3], [4, 5, 6]]))


# def cumsum(t):
#     """Computes the cumulative sum of the numbers in t.
#     t: list of numbers
#     returns: list of numbers
#     Expected output:
#     >>> t = [1, 2, 3]
#     >>> cumsum(t)
#     [1, 3, 6]
#     """
#     return


t = [1, 2, 3, 4]
def middle(t):
    return 
    
# print(middle(t))

def chop(t):
    return [t[0], t[-1]]

print(chop(t))

# def is_sorted(t):
#     """Checks whether a list is sorted.
#     t: list
#     returns: boolean
#     Expected output:
#     >>> is_sorted([1, 2, 2])
#     True
#     >>> is_sorted(['b', 'a'])
#     False
#     """
#     return


# def is_anagram(word1, word2):
#     """Checks whether two words are anagrams
#     Two words are anagrams if you can rearrange the letters from one to 
#     spell the other.
#     word1: string or list
#     word2: string or list
#     returns: boolean
#     Expected output:
#     >>> is_anagram('stop', 'pots')
#     True
#     >>> is_anagram('different', 'letters')
#     False
#     >>> is_anagram([1, 2, 2], [2, 1, 2])
#     Ture
#     """
#     return


# def has_duplicates(s):
#     """Returns True if any element appears more than once in a sequence.
#     s: string or list
#     returns: bool
#     output:
#     >>> print(has_duplicates('cba'))
#     False
#     >>> print(has_duplicates('abba'))
#     True
#     """
#     return


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
#     return


# def main():
#     t = [[1, 2], [3], [4, 5, 6]]
#     # print(nested_sum(t))

#     # t = [1, 2, 3]
#     # print(cumsum(t))

#     # t = [1, 2, 3, 4]
#     # print(middle(t))
#     # chop(t)
#     # print(t)

#     # print(is_sorted([1, 2, 2]))
#     # print(is_sorted(['b', 'a']))

#     # print(is_anagram('stop', 'pots'))
#     # print(is_anagram('different', 'letters'))
#     # print(is_anagram([1, 2, 2], [2, 1, 2]))

#     # print(has_duplicates('cba'))
#     # print(has_duplicates('abba'))


# if __name__ == '__main__':
#     main()