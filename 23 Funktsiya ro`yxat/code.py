# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 10:04:39 2024

@author: DDOS
"""
def bahola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f"Talaba {ism} ning bahosini kiriting :")
        baholar[ism]=baho
    return baholar
    
talabalar=['Ali','Vali','Anvar','Sarvar','Bobur']
baholar=bahola(talabalar[:]) # royxat nusxasini jonatish 
print(baholar)
print(talabalar)