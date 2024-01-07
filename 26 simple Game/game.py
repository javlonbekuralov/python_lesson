# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 10:21:32 2024

@author: DDOS
"""
import random
    # So`z topish o`yini #
print('Keling son topish o`yinini o`ynaymiz !')
javobim=int(input('1 dan 10 gacha bo`lgan 1 ta son o`yladim siz buni topa olasizmi > > >'))
komp_oylagan_son=random.randint(1, 10)

urinish=0;

while True:
    if javobim<komp_oylagan_son :
        print('Xato! men o`ylagan son bundan kattaroq. Yana harakat qilib ko`ring >>>')
        javobim=int(input())
        urinish=urinish+1
    elif javobim>komp_oylagan_son :
        print('Xato! men o`ylagan son bundan kichikroq. Yana harakat qilib ko`ring >>>')
        urinish=urinish+1
        javobim=int(input())
    elif javobim == komp_oylagan_son :
        urinish=urinish+1
        print(f"Topdingiz {komp_oylagan_son} sonini o`yagan edim. {urinish} ta urinishda topdingiz !")
        break
