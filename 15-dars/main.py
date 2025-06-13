# Oldindan belgilangan foydalanuvchi ma'lumotlari (oddiy misol uchun)
foydalanuvchilar = {
    "asad": "12345",
    "ali": "password123",
    "dilshod": "qwerty"
}

# Foydalanuvchidan login va parol so'rash
login = input("Loginni kiriting: ")
parol = input("Parolni kiriting: ")

# Tekshirish
if login in foydalanuvchilar:
    if foydalanuvchilar[login] == parol:
        print("Tizimga muvaffaqiyatli kirdingiz!")
    else:
        print("Parol noto‘g‘ri!")
else:
    print("Bunday login mavjud emas!")
