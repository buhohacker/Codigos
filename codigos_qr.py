
 
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import  QPixmap, QImage
from PIL import Image
from PIL.ImageQt import ImageQt
from functools import partial


###Interfaz###
Ui_MainWindow, QtBaseClass = uic.loadUiType("codigos_qr.ui")

class HilbertUI(QMainWindow):
    nombreImagenCodigo = ''
    imgCodigo = ''
    listaColores = ['black', 'white', 'red', 'cyan', 'rose', 'orange', 'blue']
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
        
        
        
    ### Funciones de carga ###
    def cargarCodigo(self):
        self.nombreImagenCodigo, _ = QFileDialog.getOpenFileName(self,"Seleccionar Codigo", "./","Imágenes (*.png *.jpg)")
        self.imgCodigo = Image.open(self.nombreImagenCodigo)
        self.ui.imagenCodigo.setPixmap(QPixmap.fromImage(ImageQt(self.imgCodigo)))

    
    def guardarCodigo(self):
        self.nombreImagenCodigo, _ = QFileDialog.getSaveFileName(self,"Seleccionar Imagen", "./" + self.nombreImagenCodigo,"Imágenes (*.png *.jpg)")
        self.imgCodigo.save(self.nombreImagenCodigo)

    def menusColores(self):
        
        for col in self.listaColores:
            
            optionCol = self.ui.ColorFondo.addAction(col)
            optionCol.triggered.connect(partial(self.cambiarColorBack, col))
            
            optionCol = self.ui.ColorCodigo.addAction(col)
            optionCol.triggered.connect(partial(self.cambiarColorCod, col))

    def cambiarColorBack(self, color):
        self.colorBack = color
        
    def cambiarColorCod(self, color):
        self.colorCod = color
        
""" Consola """    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HilbertUI()
    window.show()
    app.exec_()