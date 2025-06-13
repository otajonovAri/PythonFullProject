print( )
print("1-misol")

# sonlar = [4, 7, 10, 13, 16]

# for son in sonlar:
#     if son % 2 == 0: 
#         print(son, end=", ")

print( )
print("1-misol")


raqamlar = (12, 45, 67)

for raqam in raqamlar:
    print(raqam)



print( )
print("1-misol")


sonlar = [8, 22, 5, 17, 30]

eng_katta = sonlar[0]
eng_kichik = sonlar[0]

for son in sonlar:
    if son > eng_katta:
        eng_katta = son  
    if son < eng_kichik:
        eng_kichik = son  
print("Eng katta:", eng_katta)
print("Eng kichik:", eng_kichik)
