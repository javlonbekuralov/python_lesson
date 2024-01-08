import random

def user_name():
    # Foydalanuvchidan ismini so'ramiz
    ism = input("Ismingizni kiriting: ")

    # Ismni teskari qilamiz
    teskari_ism = ism[::-1]

    # Oxiriga 0 dan 9 gacha bo'lgan ixtiyoriy son qo'shamiz
    raqam = random.randint(0, 9)

    # Username generatsiyasi
    username = teskari_ism + str(raqam)

    return username

# Funksiyani chaqirib, natijani ekranga chiqaramiz
generatsiya_qilingan_username = user_name()
print(f"Sizning uchun generatsiya qilingan username: {generatsiya_qilingan_username}")