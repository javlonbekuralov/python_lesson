#royxat va lugat ni birlashtirish 
car0={
      'nomi':'Gentra',
      'rangi':'oq',
      'yili':2006,
      'km':90000
      }
car1={
      'nomi':'nexia',
      'rangi':'qizil',
      'yili':2016,
      'km':40000
      }
car2={
      'nomi':'matiz',
      'rangi':'qora',
      'yili':2000,
      'km':60000
      }
cars=[car0, car1, car2]

#for  car in cars:
  #  print(car['nomi'])
    
#print(cars[0]['nomi'])
maktab=[]
for i in range(10):
    oquvchi = {
        'ismi':'anvar',
        'tugilgan_y': 2000
        }
    maktab.append(oquvchi)
    
#print(maktab)
dasturchilar={
    'Sarvar':['python','c'],
    'Anvar':['html','css'],
    'Bobur':['js','go']
            
    }

for kalit,qiymat in dasturchilar.items():
    print(f"{kalit} quydagi dasturlash tillarini biladi : ")
    for key in qiymat:
        print(key)