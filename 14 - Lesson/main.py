try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid numbers!")


import math

try:
    number = float(input("Enter a number: "))
    
    if number < 0:
        raise ValueError("Negative numbers are not allowed!")
    
    root = math.sqrt(number)
    print("Square Root:", root)

except ValueError as e:
    print("Error:", e)



def divide_100_by_list(numbers):
    try:
        if not numbers:
            raise ValueError("The list is empty!")

        for num in numbers:
            if num == 0:
                raise ZeroDivisionError("Cannot divide by zero in the list!")

        results = [100 / num for num in numbers]
        print("Results:", results)

    except ValueError as ve:
        print("Error:", ve)
    except ZeroDivisionError as zde:
        print("Error:", zde)

# Test cases
divide_100_by_list([25, 0, 10])   # Error: Cannot divide by zero
# divide_100_by_list([])         # Error: The list is empty
# divide_100_by_list([10, 20])   # Results: [10.0, 5.0]
