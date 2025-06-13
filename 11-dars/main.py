print( )
print("1-misol")
class Talaba:
    def __init__(self, ism, yosh, fakultet):
        self.ism = ism
        self.yosh = yosh
        self.fakultet = fakultet
    def talaba_malumotlari(self):
        print(f"Ismi: {self.ism}, Yoshi: {self.yosh}, Fakulteti: {self.fakultet}")
talaba1 = Talaba("Ali", 20, "Dasturlash")
talaba1.talaba_malumotlari()




print( )
print("2-misol")
class Tortburchak:
    def __init__(self, uzunlik, en):
        self.uzunlik = uzunlik
        self.en = en

    def yuza(self):
        return self.uzunlik * self.en

    def perimetr(self):
        return 2 * (self.uzunlik + self.en)

t1 = Tortburchak(4, 5)
print("Yuza:", t1.yuza())
print("Perimetr:", t1.perimetr())




print( )
print("3-misol")
class Hisoblagich:
    def __init__(self):
        self.qiymat = 0  

    def oshirish(self):
        self.qiymat += 1  

    def kamaytirish(self):
        self.qiymat -= 1  

    def qaytar(self):
        return self.qiymat  

h = Hisoblagich()
h.oshirish()
h.oshirish()
h.kamaytirish()
print("Hozirgi qiymat:", h.qaytar())
