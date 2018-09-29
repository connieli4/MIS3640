fin = open('session09/words.txt')

# counter = 0
# for line in fin:
#     word = line.strip()
#     counter += 1
#     # print(word)
# print(counter)

def read_long_words():
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

# read_long_words()

def has_no_e(word):
    for letter in word:
        if letter == 'e' or letter == 'E':
            return False
    return True

# print(has_no_e('hello'))

def avoids(word, forbbiden):
    for letter in word:
        if letter == forbbiden.lower() or letter == forbbiden.upper():
            return False
    return True

# print(avoids('hello', 'O'))

def uses_only(word, available):
    for letter in word: 
        if letter not in available:
            return False
    return True

def uses_all(word, required):
    for letter in required: 
        if letter not in word:
            return False
    return True

def is_abecedarian(word):
    previous = word[0]
    for c in word:
        while c < previous:
            return False
        previous = c
    return True

is_abecedarian('hello')