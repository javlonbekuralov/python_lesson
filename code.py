#Muallif: Javlonbek
ism="Javlonbek"
print("Mening ismim "+ism)
familya="Uralov"
print(ism+" "+familya)
ism_sharif=f"{ism} {familya}" # f stringdan foydalanish
print(ism_sharif)
print(ism_sharif.upper()) # hamma harflarni katta harflarga almashtirish
print(ism_sharif.lower()) # hamma harflarni kichik harflarga almashtirish
print(ism_sharif.title()) # har bir soz boshi katta harf bilan yoziladi
print(ism_sharif.capitalize()) # faqat birinchi harf katta harf bilan yoziladi
telefon="       Redmi         "
print("Ukamga kecha ",telefon.strip()," rusumli telefon oldim !") # boshliqlarni olib tashlash

#input

name=input("Ismingizni kiriting : \n>>> ") # foydalanuvchidan malumot olish
print("Welcome ",name.capitalize())