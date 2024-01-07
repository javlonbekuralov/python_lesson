# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 09:10:26 2024

@author: DDOS
"""
# MOSLASHUVCHAN FUNKTSIYA

                              #*args     

#def summa(*sonlar):
#    yigindi=0
#    for son in sonlar:
#        yigindi=yigindi+son 
#    return yigindi

#yigindi1=summa(1,2,3,4)
#yigrindi2=summa(55,66)
#print(yigindi1)
#print(yigrindi2)

#def summa(x,y,*sonlar):
 #       return x+y+sum(sonlar)

#print(summa(1, 2, 1,2,3,4,5,6))
#print(summa(1,2,3))
#print(summa(1,2,5))    

                                #*kwargs

def avto_info(kompaniya,model,**malumotlar):
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1=avto_info('gm', 'nexia', rang='qora',yil=2000)
avto2=avto_info('ferrari', 'xyz', narx=350000)
print(avto1)
print(avto2)
