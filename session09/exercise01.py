fin = open('session09/words.txt')

#1. Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace)

def read_long_words():
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

# read_long_words()

#2. 2. In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter “e”. Since “e” is the most common letter in English, that’s not easy to do.

# Write a function called has_no_e that returns True if the given word doesn’t have the letter “e” in it.

#Modify your program from the previous section to print only the words that have no “e” and compute the percentage of the words in the list that have no “e”.

fin = open('session09/words.txt')

def find_e():
    count = 0
    for line in fin:
        word = line.strip()
        if 'e' or 'E' not in word:
                count = count + 1
        return print(count)


find_e()


#3.3. Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesn’t use any of the forbidden letters.

#Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the smallest number of words?

# def avoids(word, forbbiden):
#     for letter in word:
#         if letter in forbidden:
#             return False
#     return True

# print(avoids('Babson', 'a'))

# Exercise 2
# Rewrite is_abecedarian using recursion.
# def is_abecedarian(word):
#     n = word[0]
#     for c in word:
#         while c < n:
#             return False
#         n - 1 = c
#     return True

# is_abecedarian('hello')
# Rewrite is_abecedarian using while loop.
# def is_abecedarian(word):
#     previous = word[0]
#     for c in word:
#         while c < previous:
#             return False
#         previous = c
#     return True

# is_abecedarian('hello')


# fin = open('session09/words.txt')

# def find_trip():
#     for line in fin:
#         word = line.strip()
#         for letter in word:
#             if word[letter] == word[letter + 1] == word[letter + 2]:
#                 print(word)


# fin = open('session09/words.txt')

# def uses_all(word, required):
#     for letter in required: 
#         if letter not in word:
#             return False
#     return True

# def uses_all_vowels():
#     fin = open('session09/words.txt')
#     counter = 0
#     for line in fin:
#         word = line.strip()
#         if uses_all(word, 'aeiouy'):
#             counter += 1
#     return counter

# print(uses_all_vowels())

def is_abc(word):
    prev = word[0]
    for letter in word:
        if letter < prev:
            return False
        prev = letter
    return True 

def uses_abc():
    fin = open('session09/words.txt')
    counter = 0
    current_longest = ''
    for line in fin:
        word = line.strip()
        if is_abc(word):
            counter += 1
            if len(word) > len(current_longest):
                current_longest = word
    return counter, current_longest

print(uses_abc())