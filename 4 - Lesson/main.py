print()
print("Example 1")
number = float(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print()
print("Example 2")
grade = int(input("Enter the grade: "))
if grade >= 90:
    print("Excellent")
elif 75 <= grade <= 89:
    print("Good")
elif 50 <= grade <= 74:
    print("Satisfactory")
else:
    print("Unsatisfactory")

print()
print("Example 3")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
largest = max(num1, num2, num3)
print(f"The largest number is: {largest}")
