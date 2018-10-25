# team = 'New England Patriots'
# # letter = team[-2] 
# # # print(letter)

# # index = 0
# # while index < len(team):
# #     letter = team[index]
# #     print(letter)
# #     index = index + 1

# # prefixes = 'JKLMNOPQ'
# # suffix = 'ack'
# # for letter in prefixes:
# #     if letter == 'O' or letter == 'Q':
# #         print(letter + 'u' + suffix)
# #     else:
# #         print(letter + suffix)
# def find(word, letter):
#     index = 0
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index = index + 1
#     return -1
# print(find(team, 'E'))

# for i in range(len(team)):
#     if team[i] == 'a':
#         print(i)

# for i, letter in enumerate(team):
#     print(i, letter)

team = 'New England Patriots'
def count(s, letter):
    count = 0
    for each in s:
        if each == letter:
            count = count + 1
    return count

print(count(team, 'a'))

# team = 'New England'
# print(team.split())
