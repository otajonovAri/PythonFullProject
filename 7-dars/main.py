print( )
print("1-misol")

matn = "dasturlash juda yaxshi dasturlash"
sozlar = matn.split()
takrorlash = {}
for soz in sozlar:
    if soz in takrorlash:
        takrorlash[soz] += 1
    else:
        takrorlash[soz] = 1
print(takrorlash)


print( )
print("2-misol")

foydalanuvchi = {"ism": "Ali", "yosh": 20, "shahar": "Andijon"}
foydalanuvchi["yosh"] = 21
del foydalanuvchi["shahar"]
print(foydalanuvchi)


print( )
print("3-misol")
royxat = [1, 2, 2, 3, 4, 4, 5]
noyob_qiymatlar = set(royxat)
print(noyob_qiymatlar)
print( )
