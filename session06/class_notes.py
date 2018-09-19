# age = 10

# if age >= 18:
#     print('Your age is', age)
#     print('adult')
# else:
#     print('no')

# BMI Categories:

# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater

# weight = input('Please enter your weight: ')
# height = input('Please enter your height: ')

# def calc_BMI(weight, height):
#     BMI = weight / height
#     if BMI < 18.5:
#         print('Your BMI is', BMI)
#         print('You are underweight')
#     elif 18.5 < BMI <= 24.9:
#         print('Your BMI is', BMI)
#         print('You are normal weight')
#     elif 25 < BMI <= 29.9:
#         print('Your BMI is', BMI)
#         print('You are overweight')
#     else:
#         print('Your BMI is', BMI)
#         print('You are obese')

# print(calc_BMI)


# Assume that two variables, varA and varB, are assigned values, either numbers or strings. Write a piece of Python code that prints out one of the following messages:

# "string involved" if either varA or varB are strings
# "bigger" if varA is larger than varB
# "equal" if varA is equal to varB
# "smaller" if varA is smaller than varB

# def compare(varA, varB):
#     if isinstance(varA, str) or isinstance(varB, str):
#         print('string involved')
#     else:
#         if varA > varB:
#             print('bigger')
#         elif varA == varB:
#             print('equal')
#         else:
#             print('smaller')

# a = 4
# b = 4

# compare(a, b)

# codingbat warmup 1- diff21
# def diff21(n):
#       result = n - 21
#   abs = result * -1
#   if result <= 0:
#     return abs
#   elif n > 21:
#     return result * 2

#logic 1 cigar party
# def cigar_party(cigars, is_weekend):
#       if is_weekend and cigars >= 40 or 40 <= cigars <= 60:
#     return True
#   else:
#     return False

# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)
# countdown(8)
