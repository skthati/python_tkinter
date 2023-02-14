'''Defination showcasing how to pass multiple arguments'''
lst = []

def add(*args): # "*" is main here. with * before variable, we can pass any number of arguments to Defination
    for i in args:
        lst.append(i)
    return sum(lst)

print(add(2, 3, 4, 5, 6))
