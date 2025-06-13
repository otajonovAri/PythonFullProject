print()
print("Example 1")

for num in range(10, 101, 2):
    print(num, end=", ")

print()
print("Example 2")

number = 0
while number <= 0:
    number = int(input("Please enter a positive number: "))
    if number <= 0:
        print("Error! Enter a positive number.")

print(f"A positive number was entered: {number}")

print()
print("Example 3")

for i in range(1, 6):  
    for j in range(1, 6):
        print(i * j, end=" ")  
    print()
