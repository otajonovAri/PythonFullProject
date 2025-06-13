print( )
print("1-misol")
ism = input("Iltimos, ismingizni kiriting: ")
print(f"Salom, {ism}! Xush kelibsiz!")


print( )
print("2-misol")
from datetime import datetime
hozirgi_yil = datetime.now().year
tugilgan_yil = int(input("Tug‘ilgan yilingizni kiriting: "))
yosh = hozirgi_yil - tugilgan_yil
print(f"Siz {yosh} yoshdasiz (hozirgi yil {hozirgi_yil})")


print( )
print("3-misol")
taom = input("Iltimos, taom tanlang: ")
ichimlik = input("Iltimos, ichimlik tanlang: ")
desert = input("Iltimos, desert tanlang: ")
print("\nSiz quyidagi buyurtmani berdingiz:")
print(f"Taom: {taom}")
print(f"Ichimlik: {ichimlik}")
print(f"Desert: {desert}")
print("Yoqimli ishtaha!")
