# muallif: Javlonbek

cars=["bmw","mers","byd","audi","volvo"]

cars.sort() # royxatni harflar bo`yicha tartiblash !
print(cars)

cars.sort(reverse=True) # Teskari tartibda tartiblash 
print(cars)

#SORTED
print(sorted(cars)) # asl royxatni izmenit qilmaslik
print(cars)

#sonlar
sonlar=[1,2,3,5,4,3,666,1,0]
sonlar.sort()
print(sonlar)

print(len(sonlar)) # royxat uzunligini aniqlash

#RANGE
numbers=list(range(0,10))
print(numbers)

sonlar2=list(range(0,22,2)) # 2 qanam bilan
print(sonlar2)

#max min sum

print(max(sonlar2))
print(min(sonlar))
print(sum(sonlar))
print(sonlar[0:3]) # malum bir sonlarni chiqarish