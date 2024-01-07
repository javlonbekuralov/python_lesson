# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:20:34 2024

@author: DDOS
"""
from transliterate import to_cyrillic, to_latin
matn=input('Matn kiriting >>>')
if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))