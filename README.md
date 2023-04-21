<a name="readme-top"></a>


<div align="center">
<!-- Title: -->
<h1><a href="https://github.com/skthati/python_tkinter">tkinter</a> - Python </h1>
</div>

<!-- Table of contents -->
<hr>
<hr>
<ol>
    <li><a href="#tkinter-python">Python Basics</a></li>
    <li><a href="#bloopers">Bloopers</a></li>
</ol>
<hr>
<hr>


# tkinter python
 All basic code syntax 

```Python
import tkinter

window = tkinter.Tk()
window.title("Hello World")
window.minsize(600, 500)


my_label = tkinter.Label(text="Hello World!", font=("vardana", 23, "bold"))
my_label.pack()
tkinter.mainloop()
```

<hr>

## Multiple Args

```Python
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
```

<hr>

## Keyword Args kwargs

```Python
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
```

<hr>
## Keyword Args class

```Python
class Car:
    def __init__(self, **kwargs):
        # Below two lines can give error if you haven't passed any values.
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Toyota", model="Aqua")
print(my_car.make, my_car.model)

```


<!--
```Python

``` 
-->
<!-- 

Test1  
## Test <a name="test"></a>
Test Test

1. Code
    ```Python
    sc.onkey(key="Up", fun=up_move)
    sc.onkey(key="Right", fun=right_move)
    sc.onkey(key="Left", fun=left_move)
    sc.onkey(key="Down", fun=down_move)
    ```

2. Output

    ![Alt text](images/snake_working.gif)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<hr>  


-->

