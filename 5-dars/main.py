print( )
print("1-misol")

for son in range(10, 101, 2):
    print(son, end=", ")

print( )
print("2-misol")

son = 0  
while son <= 0:
    son = int(input("Iltimos, musbat son kiriting: "))
    if son <= 0:
        print("Xato! Musbat son kiriting.")

print(f"Musbat son kiritildi: {son}")


print( )
print("3-misol")

for i in range(1, 6):  
    for j in range(1, 6):
        print(i * j, end=" ")  
    print()  