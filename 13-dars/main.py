print( )
print("1-misol")
import birinchi_modul

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))

print("Yig'indi:", birinchi_modul.summa(a, b))
print("Ayirma:", birinchi_modul.ayirma(a, b))





print( )
print("2-misol")
from my_paket import matematika, fizika

# Matematika funksiyalari
print("5 + 3 =", matematika.summa(5, 3))
print("10 - 4 =", matematika.ayirma(10, 4))

# Fizika funksiyalari
print("Tezlik:", fizika.tezlik(100, 5))        # 100 metrni 5 sekundda
print("Kuch:", fizika.kuch(10, 9.8))           # 10kg × 9.8 m/s²






print( )
print("3-misol")
import math
import datetime

# 1. math moduli yordamida
son = 25
ildiz = math.sqrt(son)
kosinus = math.cos(math.radians(60))  # 60° ni radianlarga aylantirib hisoblash

print("Son:", son)
print("Ildizi:", ildiz)
print("60 gradusning kosinusi:", kosinus)

# 2. datetime moduli yordamida
hozirgi_vaqt = datetime.datetime.now()
print("Bugungi sana va vaqt:", hozirgi_vaqt)
