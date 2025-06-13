print( )
print("1-misol")

def full_name(ism, familiya="Familiyasi yo‘q"):
    return f"{ism} {familiya}"
print(full_name("Ali"))              
print(full_name("Ali", "Valiyev"))   

print( )
print("2-misol")

def shape_area(shape, **kwargs):
    if shape == "kvadrat":
        a = kwargs.get("a")  
        return a ** 2
    elif shape == "to'g'ri to'rtburchak":
        a = kwargs.get("a")  
        b = kwargs.get("b") 
        return a * b
    else:
        return "Shakl tanlanmadi"

print(shape_area("kvadrat", a=4))  
print(shape_area("to'g'ri to'rtburchak", a=4, b=5))  


print( )
print("3-misol")

def sum_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n - 1)

print(sum_to_n(10)) 
