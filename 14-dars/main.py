try:
    a = float(input("Birinchi sonni kiriting: "))
    b = float(input("Ikkinchi sonni kiriting: "))
    
    natija = a / b
    print("Natija:", natija)

except ZeroDivisionError:
    print("Xatolik: Nolga bo‘lish mumkin emas!")
except ValueError:
    print("Xatolik: Iltimos, faqat son kiriting!")







import math

try:
    son = float(input("Son kiriting: "))
    
    if son < 0:
        raise ValueError("Manfiy sonlar qabul qilinmaydi!")
    
    ildiz = math.sqrt(son)
    print("Ildiz:", ildiz)

except ValueError as e:
    print("Xatolik:", e)







def bolish_100ga(royxat):
    try:
        if not royxat:
            raise ValueError("Bo‘sh ro‘yxat!")

        for son in royxat:
            if son == 0:
                raise ZeroDivisionError("Nolga bo‘lish mumkin emas!")

        natijalar = [100 / son for son in royxat]
        print("Natija:", natijalar)

    except ValueError as ve:
        print("Xatolik:", ve)
    except ZeroDivisionError as zde:
        print("Xatolik:", zde)


# Test qilish:
bolish_100ga([25, 0, 10])   # Xatolik: Nolga bo‘lish mumkin emas!
# bolish_100ga([])         # Xatolik: Bo‘sh ro‘yxat!
# bolish_100ga([10, 20])   # Natija: [10.0, 5.0]
