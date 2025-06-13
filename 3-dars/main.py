print( )
print("1-misol")
narx = float(input("Mahsulot narxini kiriting: "))
foiz = float(input("Chegirma foizini kiriting: "))
chegirma = narx * (foiz / 100)
yangi_narx = narx - chegirma
print(f"\nChegirma: {int(chegirma)} so'm")
print(f"Yangi narx: {int(yangi_narx)} so'm")



print( )
print("2-misol")
import math
a = float(input("Tomon a: "))
b = float(input("Tomon b: "))
c = float(input("Tomon c: "))
perimetr = a + b + c
s = perimetr / 2
yuza = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"\nPerimetr: {perimetr}")
print(f"Yuza: {yuza:.4f}")



print( )
print("3-misol")
kredit_miqdori = float(input("Kredit miqdorini kiriting: "))
yillik_foiz_stavkasi = float(input("Yillik foiz stavkasini kiriting (%): "))
kredit_muddati = int(input("Kredit muddatini kiriting (yil): "))
yillik_foiz = kredit_miqdori * (yillik_foiz_stavkasi / 100)
umumiy_qarz = kredit_miqdori + (yillik_foiz * kredit_muddati)
print(f"\nYillik foiz: {int(yillik_foiz)}")
print(f"Umumiy qarz miqdori: {int(umumiy_qarz)}")
