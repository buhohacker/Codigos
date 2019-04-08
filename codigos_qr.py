
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

###Interfaz###
Ui_MainWindow, QtBaseClass = uic.loadUiType("codigos_qr.ui")

class HilbertUI(QMainWindow):
    nombreImagenCodigo = ''
    imgCodigo = ''
    listaColores = [('black', 'Negro'), ('white', 'Blanco'), ('red', 'Rojo'), ('cyan', 'Cian'), ('rose', 'Rosa'), ('orange', 'Naranja'), ('blue', 'Azul')]
    colorBack = 'white'
    colorCod = 'black'
    
    def __init__(self):
        super(HilbertUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.CargarCodigo.triggered.connect(self.cargarCodigo)
       
        self.ui.GuardarCodigo.triggered.connect(self.guardarCodigo)
        
        #self.ui.GenerarCodigo.clicked.connect(self.algoritmoHilbert)
        
        self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(Image.new('RGBA', (256,256), (255,255,255)))))
        
        self.menusColores()
        
        # Línea de cód para activar el botón y que llama a la función línea 
        self.ui.GenerarCodigo.clicked.connect(self.generarCod)
        
        
    ### Funciones de carga ###
    def cargarCodigo(self):
        self.nombreImagenCodigo, _ = QFileDialog.getOpenFileName(self,"Seleccionar Codigo", "./","Imágenes (*.png *.jpg)")
        self.imgCodigo = Image.open(self.nombreImagenCodigo)
        self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(self.imgCodigo)))
        
        """ TODO descifrar automaticamente al cargar ¿?"""

    
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
        """TODO Agregar cambio de color al codigo"""
        
    def cambiarColorCod(self, color):
        self.colorCod = color
        """TODO Agregar cambio de color al codigo"""
        
    """TODO metodo descifr/crear codigo"""
    def generarCod(self):
        textoCod = ''
        textoCod = self.ui.TextoCodigo
        qr = qrcode.make(textoCod)
        self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(qr)))
    
        
""" Consola """    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HilbertUI()
    window.show()
    app.exec_()