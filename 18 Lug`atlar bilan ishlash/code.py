#Lugatlar 
#car={'model':'bmw','rang':'qizil'}
#print(car['model'])
#lugat={'apple':'olma','banan':'banana'}
#print(lugat)
#mevalar={'olma':10000,'nok':500000}
#print(mevalar)
telefonlar= {
    'anvar':'redmi',
    'sarvar':'samsung',
    'bobur':'iphone',
    'temur':'poco'
   }

# get metodi

#phone=telefonlar.get('anvar','bunday kalit mavjud emas')
#print(phone)

# ITEMS

print(telefonlar.items())

for kalit,qiymat in telefonlar.items():
    print('kalit= ',kalit)
    print('qiymat= ',qiymat)
    
#keys

print(telefonlar.keys())