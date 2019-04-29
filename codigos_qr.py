
# Paquetes.
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import  QPixmap
from PIL import Image
from PIL.ImageQt import ImageQt
from functools import partial

# Paquete para trabajar con los códigos QR.
import qrcode
from pyzbar.pyzbar import decode

###Interfaz###
Ui_MainWindow, QtBaseClass = uic.loadUiType("codigos_qr.ui")

class QRcodeUI(QMainWindow):
    nombreImagenCodigo = ''
    imgCodigo = ''
    listaColores = [('black', 'Negro'), ('white', 'Blanco'), ('red', 'Rojo'), ('cyan', 'Cian'), ('pink', 'Rosa'), ('orange', 'Naranja'), ('blue', 'Azul')]
    colorBack = 'white'
    colorCod = 'black'
   
   # QR
    
    def __init__(self):
        super(QRcodeUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.CargarCodigo.triggered.connect(self.cargarCodigo)
       
        self.ui.GuardarCodigo.triggered.connect(self.guardarCodigo)
        
        #self.ui.GenerarCodigo.clicked.connect(self.algoritmoHilbert)
        
        self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(Image.new('RGBA', (256,256), (255,255,255)))))
        
        self.menusColores()        
        
        # Línea de cód para activar el botón y que llama a la función línea 
        self.ui.GenerarCodigo.clicked.connect(self.generarCod)
        
        #
        self.ui.CargarCodigo.triggered.connect(self.descifrarCod)
        
        
    ### Funciones de carga ###
    def cargarCodigo(self):
        self.nombreImagenCodigo, _ = QFileDialog.getOpenFileName(self,"Seleccionar Codigo", "./","Imágenes (*.png *.jpg)")
        self.imgCodigo = Image.open(self.nombreImagenCodigo)
        self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(self.imgCodigo)))
        qrTexto = decode(Image.open(self.nombreImagenCodigo))[0].data.decode("utf-8")
        self.ui.TextoCodigo.setText(qrTexto)

    
    def guardarCodigo(self):
        self.nombreImagenCodigo, _ = QFileDialog.getSaveFileName(self,"Seleccionar Imagen", "./" + self.nombreImagenCodigo,"Imágenes (*.png *.jpg)")
        self.imgCodigo.save(self.nombreImagenCodigo)

    #Funciones Personalizar
    def menusColores(self):
        
        for (col, colE) in self.listaColores:
            
            optionCol = self.ui.ColorFondo.addAction(colE)
            optionCol.triggered.connect(partial(self.cambiarColorBack, col))
            
            optionCol = self.ui.ColorCodigo.addAction(colE)
            optionCol.triggered.connect(partial(self.cambiarColorCod, col))

    def cambiarColorBack(self, color):
        self.colorBack = color
        
        textoCod = self.ui.TextoCodigo.toPlainText()
        qr = qrcode.QRCode()      
        qr.add_data(textoCod)
        img = qr.make_image(back_color=self.colorBack, fill_color=self.colorCod)
        self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
        """for (col, colE) in self.listaColores:
            # Color de fondo negro.
            if ((col, colE) == (color, 'Negro')):    
                img = qr.make_image(back_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de fondo blanco.
            if ((col, colE) == (color, 'Blanco')):    
                img = qr.make_image(back_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de fondo rojo.
            if ((col, colE) == (color, 'Rojo')):    
                img = qr.make_image(back_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de fondo cian.
            if ((col, colE) == (color, 'Cian')):    
                img = qr.make_image(back_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de fondo rosa.
            if ((col, colE) == (color, 'Rosa')):    
                img = qr.make_image(back_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de fondo naranja.
            if ((col, colE) == (color, 'Naranja')):    
                img = qr.make_image(back_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de fondo azul.
            if ((col, colE) == (color, 'Azul')):    
                img = qr.make_image(back_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
        """
        
    def cambiarColorCod(self, color):
        self.colorCod = color
     
        textoCod = self.ui.TextoCodigo.toPlainText()
        qr = qrcode.QRCode()      
        qr.add_data(textoCod)
        img = qr.make_image(back_color=self.colorBack, fill_color=self.colorCod)
        self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
        """
        for (col, colE) in self.listaColores:
            # Color de codigo negro.
            if ((col, colE) == (color, 'Negro')):    
                img = qr.make_image(fill_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de codigo blanco.
            if ((col, colE) == (color, 'Blanco')):    
                img = qr.make_image(fill_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de codigo rojo.
            if ((col, colE) == (color, 'Rojo')):    
                img = qr.make_image(fill_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de codigo cian.
            if ((col, colE) == (color, 'Cian')):    
                img = qr.make_image(fill_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de codigo rosa.
            if ((col, colE) == (color, 'Rosa')):    
                img = qr.make_image(fill_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de codigo naranja.
            if ((col, colE) == (color, 'Naranja')):    
                img = qr.make_image(fill_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
                
            # Color de codigo azul.
            if ((col, colE) == (color, 'Azul')):    
                img = qr.make_image(fill_color=color)
                self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
        
    """    
    """TODO metodo descifr/crear codigo"""
    def generarCod(self): 
        textoCod = self.ui.TextoCodigo.toPlainText()

        qr = qrcode.QRCode()
        qr.add_data(textoCod)

        img = qr.make_image()
        #self.QR = qr
        
        self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(img)))
    
        
    def descifrarCod(self): 
        qrTexto = decode(Image.open(self.nombreImagenCodigo))[0].data.decode("utf-8")
        self.ui.TextoCodigo.setText(qrTexto)
    
        
""" Consola """    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRcodeUI()
    window.show()
    app.exec_()