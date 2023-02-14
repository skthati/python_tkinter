'''kwargs are multiple keyword arguments.'''
'''kwargs are converted as dictionaries.'''


def calculate(n = 2, **kwargs):
    print(kwargs)
    ''' One way of calling dict is below'''
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    '''Or we can call directly'''
    print(n + kwargs["sum"])
    print(n * kwargs["multiply"])


calculate(3, sum=3, multiply=5)

# print(calculate())