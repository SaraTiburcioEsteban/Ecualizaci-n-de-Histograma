# Importar bibliotecas

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


# Instancia de la clase QApplication

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hola = None
        self.ruta = None
        self.image = None
        self.inicializar()

    def inicializar(self):
        self.hola = QPushButton('hola')
        self.setCentralWidget(self.hola)
        self.show()

    def hola(self):
        img_name = QFileDialog.getOpenFileName(self, 'Abrir archivo', '/home/', '*.tif *.jpg *.png *.jpeg')
        self.ruta = img_name[0]
        orig_pix_map = QPixmap(self.ruta)
        scaled_pix_map = orig_pix_map.scaled(QSize(400, 400), Qt.AspectRatioMode.KeepAspectRatio)
        self.image.setPixmap(scaled_pix_map)


# Iniciar el ciclo de eventos

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ventana()
    sys.exit(app.exec())
