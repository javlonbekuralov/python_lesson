# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 10:04:02 2024

@author: DDOS
"""
#             Fayllar bilan ishlash

#fayl = open('pi.txt.txt')
#pi_soni = fayl.read()
#print(pi_soni)
#fayl.close()
        # bu usul tavsiya qilinmaydi !!!
        
        # tavsiya qilingan usul #

#with open('pi.txt') as file :
 #   pi= file.read()


#pi=pi.rstrip()
#pi=pi.replace('\n', '')
#pi=float(pi)
#print(pi)

            # file bilan ishlash #
filename='data/talabalar.txt'
#with open(filename) as file:
 #   for line in file:
  #      print(f"talaba - >  {line}")
   
                # royxatga joylash #
with open(filename) as file:
    talabalar=file.readlines()
print(talabalar)
                    #boshliqlarni olib tashlash#
talabalar=[oquvchi.rstrip() for oquvchi in talabalar]
print(talabalar)

    