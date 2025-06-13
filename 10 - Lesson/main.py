print()
print("Example 1")

def write_student_grades():
    n = int(input("How many student records will you enter? "))
    with open("grades.txt", "w") as file:
        for _ in range(n):
            name, grade = input("Enter student name and grade (e.g., Ali 85): ").split()
            file.write(f"{name} {grade}\n")

def extract_top_students():
    with open("grades.txt", "r") as file:
        top_students = []
        for line in file:
            name, grade = line.split()
            grade = int(grade)
            if grade >= 90:
                top_students.append(f"{name} - {grade}\n")
    
    with open("top_students.txt", "w") as file:
        file.writelines(top_students)

write_student_grades()
extract_top_students()
print("Top students have been written to a separate file!")



print()
print("Example 2")

from collections import Counter

def text_statistics():
    try:
        with open("C:/Users/user/Desktop/python vazifalar/10-dars/matn.txt", "r") as file:
            text = file.read().lower()
    except FileNotFoundError:
        print("File not found!")
        return

    if not text.strip():
        print("Text is empty!")
        return

    words = text.split()
    total_words = len(words)
    unique_words = len(set(words))
    word_counts = Counter(words)

    if word_counts:
        most_common = word_counts.most_common(1)[0]
        print(f"Most frequent word: '{most_common[0]}' ({most_common[1]} times)")
    else:
        print("No words found.")

    print(f"Total number of words: {total_words}")
    print(f"Number of unique words: {unique_words}")

text_statistics()


print()
print("Example 3")

def number_statistics():
    try:
        with open("C:/Users/user/Desktop/python vazifalar/10-dars/raqamlar.txt", "r") as file:
            numbers = [int(num) for line in file.readlines() for num in line.split()]
    except FileNotFoundError:
        print("File not found!")
        return
    except ValueError:
        print("Invalid data format in file!")
        return

    if not numbers:
        print("No numbers found in the file!")
        return

    max_num = max(numbers)
    min_num = min(numbers)
    average = sum(numbers) / len(numbers)
    even_sum = sum(num for num in numbers if num % 2 == 0)

    print(f"Largest number: {max_num}")
    print(f"Smallest number: {min_num}")
    print(f"Average: {average:.2f}")
    print(f"Sum of even numbers: {even_sum}")

number_statistics()
