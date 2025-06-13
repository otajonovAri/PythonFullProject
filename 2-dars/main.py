print( )
print("1-misol")
matn = input("Matnni kiriting: ")
uzunlik = len(matn)
print(f"\nMatn uzunligi: {uzunlik} ta belgidan iborat")
print("Katta harflar bilan:", matn.upper())
print("Kichik harflar bilan:", matn.lower())



print( )
print("2-misol")
from datetime import datetime
hozirgi_yil = datetime.now().year
ism = input("Ismingizni kiriting: ")
familiya = input("Familiyangizni kiriting: ")
tugilgan_yil = int(input("Tug‘ilgan yilingizni kiriting: "))
yosh = hozirgi_yil - tugilgan_yil
print("\nSizning shaxsiy profilingiz:")
print(f"Ism: {ism}")
print(f"Familiya: {familiya}")
print(f"Tug‘ilgan yil: {tugilgan_yil}")
print(f"Yosh: {yosh} yosh")



print( )
print("3-misol")
gap = input("Biror gap kiriting: ")
sozlar = gap.split()
soni = len(sozlar)
eng_uzun_soz = max(sozlar, key=len)
print(f"\nSo‘zlar soni: {soni} ta")
print(f"Eng uzun so‘z: {eng_uzun_soz}")
