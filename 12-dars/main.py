print( )
print("1-misol")
class Avtomobil:
    def __init__(self, model, yil, tezlik):
        self.model = model
        self.yil = yil
        self.tezlik = tezlik

    def harakatlan(self):
        print(f"{self.model} avtomobili harakatlanmoqda!")

class Elektromobil(Avtomobil):
    def __init__(self, model, yil, tezlik, batareya_quvvati):
        super().__init__(model, yil, tezlik)  
        self.batareya_quvvati = batareya_quvvati

    def harakatlan(self):
        print(f"{self.model} elektromobili harakatlanmoqda! Batareya: {self.batareya_quvvati}")

a1 = Elektromobil("Tesla", 2023, 150, "100 kWh")
a1.harakatlan()





print( )
print("2-misol")
class Shakl:
    def yuza(self):
        pass  

class Doira(Shakl):
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return 3.14 * self.radius ** 2  

class Kvadrat(Shakl):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon * self.tomon  

figuralar = [
    Doira(5),
    Kvadrat(5)
]

for shakl in figuralar:
    if isinstance(shakl, Doira):
        print(f"Doira yuzi: {shakl.yuza()}")
    elif isinstance(shakl, Kvadrat):
        print(f"Kvadrat yuzi: {shakl.yuza()}")





print( )
print("3-misol")
class BankHisobi:
    def __init__(self):
        self.__balans = 0  

    def deposit(self, summa):
        self.__balans += summa
        print(f"Hisobga {summa} qo‘shildi.")

    def withdraw(self, summa):
        if summa > self.__balans:
            print("Balansda yetarli mablag‘ yo‘q.")
        else:
            self.__balans -= summa
            print(f"{summa} so‘m yechildi. Yangi balans: {self.__balans}")

    def balansni_ol(self):
        return self.__balans


class BiznesHisob(BankHisobi):
    def withdraw(self, summa):
        komissiya = summa * 0.05
        jami = summa + komissiya
        if jami > self.balansni_ol():
            print("Balansda yetarli mablag‘ yo‘q.")
        else:
           

            self._BankHisobi__balans -= jami  

            print(f"{summa} so‘m yechildi (komissiya bilan {int(jami)}). Yangi balans: {int(self._BankHisobi__balans)}")


hisob = BiznesHisob()
hisob.deposit(1000)
hisob.withdraw(100)
