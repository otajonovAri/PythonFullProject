print()
print("Example 1")

def full_name(first_name, last_name="No last name"):
    return f"{first_name} {last_name}"

print(full_name("Ali"))
print(full_name("Ali", "Valiyev"))

print()
print("Example 2")

def shape_area(shape, **kwargs):
    if shape == "square":
        a = kwargs.get("a")
        return a ** 2
    elif shape == "rectangle":
        a = kwargs.get("a")
        b = kwargs.get("b")
        return a * b
    else:
        return "Shape not recognized"

print(shape_area("square", a=4))
print(shape_area("rectangle", a=4, b=5))

print()
print("Example 3")

def sum_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n - 1)

print(sum_to_n(10))
