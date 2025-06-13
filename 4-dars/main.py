print( )
print("1-misol")
son = float(input("Sonni kiriting: "))
if son > 0:
    print("Musbat son.")
elif son < 0:
    print("Manfiy son.")
else:
    print("Son nolga teng.")



print( )
print("2-misol")
baho = int(input("Bahoni kiriting: "))
if baho >= 90:
    print("A'lo")
elif 75 <= baho <= 89:
    print("Yaxshi")
elif 50 <= baho <= 74:
    print("Qoniqarli")
else:
    print("Qoniqarsiz")



print( )
print("3-misol")
son1 = float(input("Birinci sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))
son3 = float(input("Uchinchi sonni kiriting: "))
eng_katta = max(son1, son2, son3)
print(f"Eng katta son: {eng_katta}")
