fin = open('session09/words.txt')

def cartalk(words):
    for word in words:
        i = 0
        pairCount = 0
        while i < len(word) - 1:
            if word[i] == word[i + 1]:
                pairCount += 1
                if pairCount == 3:
                    print(word)
                i += 2
            else:
                pairCount = 0
                i += 1

cartalk('abyss')