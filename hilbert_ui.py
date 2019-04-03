
 
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5 import uic
from PyQt5.QtGui import  QPixmap, QImage
from PIL import Image
from PIL.ImageQt import ImageQt


###Interfaz###
Ui_MainWindow, QtBaseClass = uic.loadUiType("h.ui")

class HilbertUI(QMainWindow):
    nombreImagen = ''
    nombreImagenGris = ''
    nombreImagenHilbert = ''
    nombreImagenLinear = ''
    img = ''
    imgGris = ''
    imgHilbert = ''
    imgLinear = ''
    imgGrisPixel = ''
    imgHilbertPixel = ''
    imgLinearPixel = ''
    iteraciones = 0
    tamano = 0
    
    def __init__(self):
        super(HilbertUI, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Cargar_Imagen.triggered.connect(self.cargarImagen)
       
        self.ui.Guardar_Gris.triggered.connect(self.guardarImagenGris)
        self.ui.Guardar_Hilbert.triggered.connect(self.guardarImagenHilbert)
        self.ui.Guardar_Linear.triggered.connect(self.guardarImagenLinear)
        
        self.ui.boton_Hilbert.clicked.connect(self.algoritmoHilbert)
        self.ui.boton_Linear.clicked.connect(self.algoritmoLinear)
        
        self.ui.imagenOriginal.setPixmap(QPixmap.fromImage(ImageQt(Image.new('RGBA', (256,256), (255,255,255)))))
        self.ui.imagenHilbert.setPixmap(QPixmap.fromImage(ImageQt(Image.new('RGBA', (256,256), (255,255,255)))))
        self.ui.imagenLinear.setPixmap(QPixmap.fromImage(ImageQt(Image.new('RGBA', (256,256), (255,255,255)))))
    
    ### Funciones de carga ###
    def cargarImagen(self):
        self.nombreImagen, _ = QFileDialog.getOpenFileName(self,"Seleccionar Imagen", "./","Imágenes (*.png *.jpg)")
        self.img = Image.open(self.nombreImagen)
        
        self.nombreImagenGris = self.nombreImagen[:(len(self.nombreImagen)-4)] + '_g' + self.nombreImagen[(len(self.nombreImagen)-4):]
        self.tamanoImagen()
        self.imgGris = self.img.convert('L').resize((self.tamano,self.tamano),Image.ANTIALIAS)
        self.imgGrisPixel = self.imgGris.load()
        
        self.ui.imagenOriginal.setPixmap(QPixmap.fromImage(QImage(self.img.resize((256,256),Image.ANTIALIAS).convert("RGB").tobytes("raw", "RGB"),256,256,QImage.Format_RGB888)))
        self.ui.imagenHilbert.setPixmap(QPixmap.fromImage(ImageQt(Image.new('RGBA', (256,256), (255,255,255)))))
        self.ui.imagenLinear.setPixmap(QPixmap.fromImage(ImageQt(Image.new('RGBA', (256,256), (255,255,255)))))
        
        self.ui.boton_Hilbert.setEnabled(1)
        self.ui.boton_Linear.setEnabled(1)
        self.ui.Guardar_Gris.setEnabled(1)
        self.ui.Guardar_Hilbert.setEnabled(0)
        self.ui.Guardar_Linear.setEnabled(0)
        
    
    def guardarImagenGris(self):
        self.nombreImagenGris, _ = QFileDialog.getSaveFileName(self,"Seleccionar Imagen", "./" + self.nombreImagenGris,"Imágenes (*.png *.jpg)")
        self.imgGris.save(self.nombreImagenGris)
    
    def guardarImagenHilbert(self):
        self.nombreImagenHilbert, _ = QFileDialog.getSaveFileName(self,"Seleccionar Imagen", "./" + self.nombreImagenHilbert,"Imágenes (*.png *.jpg)")
        self.imgHilbert.save(self.nombreImagenHilbert)
    
    def guardarImagenLinear(self):
        self.nombreImagenLinear, _ = QFileDialog.getSaveFileName(self,"Seleccionar Imagen", "./" + self.nombreImagenLinear,"Imágenes (*.png *.jpg)")
        self.imgLinear.save(self.nombreImagenLinear)
    

    ### Funciones algoritmo ###
    def tamanoImagen(self):
  
        tam = 0
        x,y = self.img.size
        p = 1
        var = 2**p
        
        if x >= y:
            tam = x
        else:
            tam = y
            
        while tam > var:
            p += 1
            var *= 2
            
        self.iteraciones = p
        self.tamano = var
    
    def algoritmoHilbert(self):
        
        self.nombreImagenHilbert = self.nombreImagen[:(len(self.nombreImagen)-4)] + '_h' + self.nombreImagen[(len(self.nombreImagen)-4):]
        self.imgHilbert = Image.new('L', (self.tamano,self.tamano), 255)
        self.imgHilbertPixel = self.imgHilbert.load()
        
        listaHilbert = hilbert(self.iteraciones, [[0,1],[1,0],[0,-1]])
        x = 0
        y = self.tamano - 1
        
        
        
        e = 0
        o = 0
        
        ## Iteraciones de la curva
        for cont in range((self.tamano * self.tamano) - 1):
            pixel = self.imgGrisPixel[x,y]/255
            pix = pixel + e
            
            if pix <= 0.5:
                self.imgHilbertPixel[x,y] = 0
                o = 0
            else:
                self.imgHilbertPixel[x,y] = 255
                o = 1
                
            e = pixel - o + e
                    
            direc = listaHilbert[cont]
            x += direc[0]
            y -= direc[1]
            
        self.ui.imagenHilbert.setPixmap(QPixmap.fromImage(QImage(self.imgHilbert.resize((256,256),Image.ANTIALIAS).convert("RGB").tobytes("raw", "RGB"),256,256,QImage.Format_RGB888)))
        self.ui.Guardar_Hilbert.setEnabled(1)
                
    
    def algoritmoLinear(self):
        self.nombreImagenLinear = self.nombreImagen[:(len(self.nombreImagen)-4)] + '_l' + self.nombreImagen[(len(self.nombreImagen)-4):]
        self.imgLinear = Image.new('L', (self.tamano,self.tamano), 255)
        self.imgLinearPixel = self.imgLinear.load()
        
        for x in range(self.tamano - 1):
            for y in range(self.tamano - 1):
                pixel = self.imgGrisPixel[x,y]/255
                
                if pixel <= 0.5:
                    self.imgLinearPixel[x,y] = 0
                else:
                    self.imgLinearPixel[x,y] = 255
        self.ui.imagenLinear.setPixmap(QPixmap.fromImage(QImage(self.imgLinear.resize((256,256),Image.ANTIALIAS).convert("RGB").tobytes("raw", "RGB"),256,256,QImage.Format_RGB888)))
        self.ui.Guardar_Linear.setEnabled(1)          
        
        
### Funciones de curva ###
def giroDerecha(direccion):
         
    aux = []
    aux.append(direccion[1])
    aux.append(direccion[0])
    
    return aux
    
def giroIzquierda(direccion):
        
    aux = []
    aux.append(direccion[1]*(-1))
    aux.append(direccion[0]*(-1))
    
    return aux
    
    
def giraListaDerecha(lista):
    
    aux = []
        
    for x in lista:
        aux.append(giroDerecha(x))
        
    return aux


def giraListaIzquierda(lista):
    
    aux = []
        
    for x in lista:
        aux.append(giroIzquierda(x))        
    return aux
    
    
def iteracionHilbert(lista):
        
    aux = []
    aux = aux + giraListaDerecha(lista)
    aux.append([0,1])
    aux = aux + lista
    aux.append([1,0])
    aux = aux + lista
    aux.append([0,-1])
    aux = aux + giraListaIzquierda(lista)
    
    return aux

def hilbert(iteraciones, lista):

    aux = lista
        
    if iteraciones > 1:
        aux = iteracionHilbert(aux)
        aux = hilbert(iteraciones - 1, aux)
    return aux       
""" Consola """    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HilbertUI()
    window.show()
    app.exec_()