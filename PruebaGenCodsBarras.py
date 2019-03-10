# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 09:04:08 2019

@author: Andrea
"""

import barcode
from barcode.writer import ImageWriter


#ean = barcode.get('ean13', '123456789102')
#ean.get_fullcode()
#filename = ean.save('ean13')
#options = dict(compress=True)
#filename = ean.save('ean13', options)

ean = barcode.get('ean13', '123456789102', writer=ImageWriter())
filename = ean.save('ean13')


isbn = barcode.get('isbn13', '978456789102', writer=ImageWriter())
filename = isbn.save('isbn13')

code = barcode.get('code39', '54789489567', writer=ImageWriter())
filename = code.save('code39')