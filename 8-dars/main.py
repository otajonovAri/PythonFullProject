print( )
print("1-misol")

def qoshish(a, b):
    return a + b
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
natija = qoshish(a, b)
print("Natija:", natija)


print( )
print("2-misol")
def is_palindrome(matn):
    return matn == matn[::-1]

kirish = input("Matn kiriting: ")

natija = is_palindrome(kirish)
print("Palindrome:", natija)



print( )
print("3-misol")

def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

n = int(input("n sonini kiriting: "))
natija = faktorial(n)
print(f"{n}! =", natija)
