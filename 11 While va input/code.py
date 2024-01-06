# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 22:21:35 2024

@author: DDOS
"""
#  input

#ism=input('ismingiz kim ?')
#savol=f"{ism} yoshingiz nechada ?"
#yosh=input(savol)

#  while
#son=1
#while son < 10 :
#    print('++ + ++')
#    son=son+1



print('dostlaringiz royxatini tuzamiz >>')

dostlar=[]
for dost in range(10):
    dostlar.append(input('dostingizning ismini kiriting ='))
    dost=dost+1
    takrorlarlash=input('yana kiritasizmi ha/yoq')
    if takrorlarlash != 'ha':
        break