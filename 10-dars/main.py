print( )
print("1-misol")
def talaba_baholarini_yozish():
    n = int(input("Nechta talaba ma'lumotlarini kiritasiz? ")) 
    with open("imtihon.txt", "w") as fayl:
        for _ in range(n):
            ism, baho = input("Talabaning ismini va bahosini kiriting (masalan, Ali 85): ").split()
            fayl.write(f"{ism} {baho}\n")  

def alochilarni_ajratish():
    with open("imtihon.txt", "r") as fayl:
        alochilar = []  
        for satr in fayl:
            ism, baho = satr.split()
            baho = int(baho)  
            if baho >= 90:
                alochilar.append(f"{ism} - {baho}\n")  
    with open("alochilar.txt", "w") as fayl:
        fayl.writelines(alochilar)  

talaba_baholarini_yozish() 
alochilarni_ajratish()  
print("A'lochilar alohida faylga yozildi!")




print( )
print("2-misol")
from collections import Counter
def matn_statistikasi():
    try:
        # Faylni o‘qish
        with open("C:/Users/user/Desktop/python vazifalar/10-dars/matn.txt", "r") as fayl:
            matn = fayl.read().lower()  # Matnni kichik harflar bilan o‘qish
    except FileNotFoundError:
        print("Fayl topilmadi!")
        return
    
    if not matn.strip():
        print("Matn bo‘sh!")
        return
    sozlar = matn.split()
    
    jami_sozlar = len(sozlar)
    
    takrorlanmas_sozlar = len(set(sozlar))
    sozlar_count = Counter(sozlar)
    if sozlar_count:
        eng_kop_uchradi = sozlar_count.most_common(1)[0]  # eng ko‘p uchragan so‘z va uning soni
        print(f"Eng ko‘p uchragan so‘z: '{eng_kop_uchradi[0]}' ({eng_kop_uchradi[1]} marta)")
    else:
        print("So‘zlar mavjud emas.")
    
    print(f"Jami sozlar soni: {jami_sozlar}")
    print(f"Takrorlanmas so‘zlar soni: {takrorlanmas_sozlar}")

matn_statistikasi()





print( )
print("3-misol")
def sonlar_statistikasi():
    try:
        with open("C:/Users/user/Desktop/python vazifalar/10-dars/raqamlar.txt", "r") as fayl:
            sonlar = [int(son) for line in fayl.readlines() for son in line.split()]
    except FileNotFoundError:
        print("Fayl topilmadi!")
        return
    except ValueError:
        print("Faylda noto‘g‘ri formatdagi ma'lumot bor!")
        return
    
    if not sonlar:
        print("Faylda hech qanday son yo‘q!")
        return
    
    eng_katta = max(sonlar)
    
    eng_kichik = min(sonlar)
    
    ortacha = sum(sonlar) / len(sonlar)
    
    juft_yigindi = sum(son for son in sonlar if son % 2 == 0)
    
    print(f"Eng katta son: {eng_katta}")
    print(f"Eng kichik son: {eng_kichik}")
    print(f"O‘rtacha: {ortacha:.2f}")
    print(f"Juft sonlar yig'indisi: {juft_yigindi}")

sonlar_statistikasi()
