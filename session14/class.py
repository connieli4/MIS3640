# import random
# pool=list(range(1,71))
# random.sample(pool, 5)

# import os
# print(os.getcwd())

# fout = open('output.txt', 'a')

# line1 = "How many roads must a man walk down\n"
# fout.write(line1)

# line2 = "Before you call him a man?\n"
# fout.write(line2)
# fout.close()

# print(os.path.abspath('session12/output.txt'))
# print(os.path.exists('session14/input.txt'))

# import pickle
# t = [1, 2, 3]

# f = open('save.p', 'wb')
# s = pickle.dump(t, f)
# f.close()


# t2 = pickle.load(open('save.p', 'rb'))
# print(t2)


def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print(linecount('wc.py'))

if __name__ == '__main__':
    print(linecount('wc.py'))