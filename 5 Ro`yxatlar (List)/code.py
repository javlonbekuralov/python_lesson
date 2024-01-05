# Muallif : Javlonebek
# List lar bilan ishlash !
telefonlar=['Redmi note 10','Iphone 12','Black Shark 5 pro','Nokia 1202']
narxlar=[1000000,2000000,5000000,100000]
print(telefonlar)
print("1-telefon ",telefonlar[0]) # list elementini tanlab olish
print(telefonlar[1].upper()) # string uchun yozilgan funktsiyalardan foydalanish

#append
telefonlar.append('Samsung s8') # List ohirgiga element qoshish
print(telefonlar)

#insert

telefonlar.insert(0, 'Poco f5') #indexga asoslanib qo`shish 
print(telefonlar)

#del

del telefonlar[0]
print(telefonlar)

#remove

telefonlar.remove('Nokia 1202') # qiymatga asosan ochirish
print(telefonlar)

bozorlik=["Un","Choy","Shakar"]
mahsulot=bozorlik.pop(0)
print(bozorlik)
