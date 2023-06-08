class Vehicle:
    def __init__(self, wheels, capacity, model, price, color, build_year):
        self.wheels = wheels
        self.capacity = capacity
        self.model = model
        self.price = price
        self.color = color
        self.build_year = build_year

    def __str__(self):
        return f"{self.model} - {self.color} - {self.build_year}"


class Airplane(Vehicle):
    def __init__(self, capacity, model, price, color, build_year):
        super().__init__(0, capacity, model, price, color, build_year)


class Moto(Vehicle):
    def __init__(self, model, price, color, build_year):
        super().__init__(2, 2, model, price, color, build_year)

    def is_popular(self):
        return self.price < 5000


class Car(Vehicle):
    def __init__(self, model, price, color, build_year):
        super().__init__(4, 5, model, price, color, build_year)

    def is_popular(self):
        return self.price < 15000


car1 = Car("AAA", 10000, "orange", 2015)
car2 = Car("BBB", 15000, "blue", 2018)
car3 = Car("CCC", 45000, "green", 2015)

print(car1.model, car1.price, car1.color, car1.build_year)
print(car2.model, car2.price, car2.color, car2.build_year)
print(car3.model, car3.price, car3.color, car3.build_year)

car1.color = "red"
print(car1.model, car1.price, car1.color, car1.build_year)

print(car1.is_popular())
print(car2.is_popular())
print(car3.is_popular())

print(car1)
print(car2)
print(car3)
