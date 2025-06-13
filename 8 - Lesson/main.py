print()
print("Example 1")

def add(a, b):
    return a + b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = add(a, b)
print("Result:", result)

print()
print("Example 2")

def is_palindrome(text):
    return text == text[::-1]

input_text = input("Enter a text: ")
result = is_palindrome(input_text)
print("Is palindrome:", result)

print()
print("Example 3")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter a number (n): "))
result = factorial(n)
print(f"{n}! =", result)
