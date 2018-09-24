import math

# def my_sqrt(a):
#     x = 2
#     while True:
#         y = (x + a/x) / 2
#         if y == x:
#             break
#         x = y
#     print(y)

# def estimate_sqrt():
#     for a in range (1, 10):
#         print(my_sqrt(a))

# estimate_sqrt()

def real_sqrt():
    for i in range (1, 10):
        print(math.sqrt(i))

# real_sqrt()

list_real_sqrt = list(real_sqrt())
print(list_real_sqrt)
# def sqrt_diff():
#     print(estimate_sqrt() - real_sqrt())


