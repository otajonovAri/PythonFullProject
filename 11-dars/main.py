print()
print("Example 1")

class Student:
    def __init__(self, name, age, faculty):
        self.name = name
        self.age = age
        self.faculty = faculty

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Faculty: {self.faculty}")

student1 = Student("Ali", 20, "Programming")
student1.display_info()



print()
print("Example 2")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

r1 = Rectangle(4, 5)
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())



print()
print("Example 3")

class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def get_value(self):
        return self.value

c = Counter()
c.increment()
c.increment()
c.decrement()
print("Current value:", c.get_value())
