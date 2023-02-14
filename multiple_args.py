'''Defination showcasing how to pass multiple arguments'''
lst = []


def add(*args): # "*" is main here. with * before variable, we can pass any number of arguments to Defination
    for i in args:
        lst.append(i)
        # print(type(i))
    return sum(lst)


def add1(*args):
    x = 0
    for i in args:
        x += i
    return x


print(add(2, 3, 4, 5, 6))

print(add1(1, 2, 3, 4, 5, 6))

