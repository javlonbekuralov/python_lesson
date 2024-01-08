# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 11:06:40 2024

@author: DDOS
"""
                         # filga yozish yangi fayl#
#filename = 'new_file.txt'
#ism = 'Uralov Javlonbek'
#tyil = 1998
#with open(filename,'w') as file:
 #   file.write(ism+'\n')
 #   file.write(str(tyil))
#with open(filename,'a') as file:
#    file.write('\nBahodirova Hilola\n')
#    file.write(str(2023))

                        #pickle#
import pickle

talaba1={
    'ism':'Hilol',
    'Familya':'Bahodirova',
    'tyil':2023
    }        

talaba2={
    'ism':'Javlonbek',
    'Familya':'Uralov',
    'tyil':1998
    }
with open('info','wb') as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)

with open('info','rb') as file:
        talaba1=pickle.load(file)
        talaba2=pickle.load(file)
print(talaba1)
print(talaba2)