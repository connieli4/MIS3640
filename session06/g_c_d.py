# import math

# def find_gcd(x, y):
#     result = math.gcd(x,y)
#     if result > 1 and isinstance(result, int) == True:
#         print(result)
#     else:
#         print(1)

# find_gcd(2, 12)
# find_gcd(6, 12)
# find_gcd(9, 12)
# find_gcd(17, 12)

def gcd(a, b):
    print('Current a, b:', a, b)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

gcd(2, 12)