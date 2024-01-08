# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:09:00 2024

@author: DDOS
"""

import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('javlonbek','uralov')
        self.assertEqual(name,'Javlonbek Uralov')
unittest.main()