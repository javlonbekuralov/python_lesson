# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:44:24 2024

@author: DDOS
"""
# python da class yaratish 
class Talaba:

    def __init__(self,ism,familya,tyil):
        #talaba xususiyatlari
        self.ism=ism
        self.familya=familya
        self.tyil=tyil
        self.bosqich=1  
    
    def set_bosqich(self,yangi_bosqich):
        self.bosqich=yangi_bosqich
        
    def  get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familya
    
    def get_age(self,yil):
        return yil-self.tyil
    def set_update(self):
        self.bosqich=self.bosqich+1
        return self.bosqich
    def get_info(self):
         return (f"{self.ism} hozirda {self.bosqich} talabasi")
        
talab1=Talaba("Javlonbek", "Uralov", 1998)
talab1.set_bosqich(2)
talab1.set_update()
#print(talab1.get_info())


        