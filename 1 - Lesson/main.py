print()
print("Example 1")
name = input("Please enter your name: ")
print(f"Hello, {name}! Welcome!")

print()
print("Example 2")
from datetime import datetime
current_year = datetime.now().year
birth_year = int(input("Enter your birth year: "))
age = current_year - birth_year
print(f"You are {age} years old (Current year is {current_year})")

print()
print("Example 3")
food = input("Please choose a dish: ")
drink = input("Please choose a drink: ")
dessert = input("Please choose a dessert: ")
print("\nYou have ordered the following:")
print(f"Dish: {food}")
print(f"Drink: {drink}")
print(f"Dessert: {dessert}")
print("Enjoy your meal!")
