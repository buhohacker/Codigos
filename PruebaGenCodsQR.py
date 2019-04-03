# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 08:37:19 2019

@author: Andrea
"""

### PRUEBA DE LA GENERACIÓN DE CÓDIGOS QR. ###

import qrcode  # Importamos el modulo necesario para trabajar con codigos QR
import qrtools
import pyqrcode
#from PIL import Image

###  QR 1.  ###
imagen = qrcode.make('Hola mundo!')  # Creamos un codigo a partir de una cadena de texto

archivo_imagen = open('codigo.png', 'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()


###  QR 2.  ###
imagen2 = qrcode.make('Esto es una prueba de codigos QR.')  # Creamos un codigo a partir de una cadena de texto

archivo_imagen2 = open('codigo2.png', 'wb')
imagen2.save(archivo_imagen2)
archivo_imagen2.close()


###  QR 3.  ###
#  Creamos un objeto codigo QR
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4
)
# Podemos crear la informacion que queremos 
# en el codigo de manera separada
info = 'Necesitamos guardar este texto en el codigo QR'
# Agregamos la informacion
qr.add_data(info)
qr.make(fit=True)
# Creamos una imagen para el objeto código QR
imagen3 = qr.make_image()
# Guardemos la imagen con la extension que queramos
imagen3.save('codigo3.png')



qr = qrcode.QRCode(
    version=1,
    #error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Me encanta el rosa')
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="pink")
archivo_imagen2 = open('patata.png', 'wb')
img.save(archivo_imagen2)
archivo_imagen2.close()

###  Decodificación de un código QR.  ###
#qr = pyqrcode.create("HORN O.K. PLEASE.")
#qr.png("horn.png", scale=6)
#
#qr = qrtools.QR()
#qr.decode("horn.png")
#print (qr.data)



