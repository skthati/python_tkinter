class Car:
    def __init__(self, **kwargs):
        # Below two lines can give error if you haven't passed any values.
        # self.make = kwargs["make"]
        # self.model = kwargs["model"]
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")


my_car = Car(make="Toyota", model="Aqua")
print(my_car.make, my_car.model)