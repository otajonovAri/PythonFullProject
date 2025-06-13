print()
print("Example 1")

# Even numbers from a list (commented example)
# numbers = [4, 7, 10, 13, 16]
# for number in numbers:
#     if number % 2 == 0:
#         print(number, end=", ")

print()
print("Example 2")

digits = (12, 45, 67)

for digit in digits:
    print(digit)

print()
print("Example 3")

numbers = [8, 22, 5, 17, 30]

max_number = numbers[0]
min_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print("Maximum:", max_number)
print("Minimum:", min_number)
