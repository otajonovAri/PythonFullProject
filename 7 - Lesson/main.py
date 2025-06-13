print()
print("Example 1")

text = "programming is very good programming"
words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

print()
print("Example 2")

user = {"name": "Ali", "age": 20, "city": "Andijon"}
user["age"] = 21
del user["city"]
print(user)

print()
print("Example 3")

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_values = set(numbers)
print(unique_values)

print()
