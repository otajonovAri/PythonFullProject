print()
print("Example 1")

class Car:
    def __init__(self, model, year, speed):
        self.model = model
        self.year = year
        self.speed = speed

    def move(self):
        print(f"{self.model} car is moving!")

class ElectricCar(Car):
    def __init__(self, model, year, speed, battery_capacity):
        super().__init__(model, year, speed)  # call parent class constructor
        self.battery_capacity = battery_capacity

    def move(self):  # overriding parent method
        print(f"{self.model} electric car is moving! Battery: {self.battery_capacity}")

car1 = ElectricCar("Tesla", 2023, 150, "100 kWh")
car1.move()



print()
print("Example 2")

class Shape:
    def area(self):
        pass  # abstract method

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

shapes = [
    Circle(5),
    Square(5)
]

for shape in shapes:
    if isinstance(shape, Circle):
        print(f"Circle area: {shape.area()}")
    elif isinstance(shape, Square):
        print(f"Square area: {shape.area()}")



print()
print("Example 3")

class BankAccount:
    def __init__(self):
        self.__balance = 0  # private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, New balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

class BusinessAccount(BankAccount):
    def withdraw(self, amount):
        fee = amount * 0.05
        total = amount + fee
        if total > self.get_balance():
            print("Insufficient balance.")
        else:
            self._BankAccount__balance -= total  # access to private variable with name mangling
            print(f"Withdrawn: {amount} (with fee {int(total)}), New balance: {int(self._BankAccount__balance)}")

account = BusinessAccount()
account.deposit(1000)
account.withdraw(100)
