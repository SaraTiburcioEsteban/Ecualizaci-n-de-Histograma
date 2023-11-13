# Importar bibliotecas

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QFileDialog,
                             QHBoxLayout, QLabel, QWidget)


# Instancia de la clase QApplication

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializar()
        self.setWindowTitle('Ecualización de histrograma')
        self.setMaximumSize(QSize(1080, 720))


    def inicializar(self):
        boton_hola = QPushButton('hola')
        boton_hola.setFixedSize(QSize(100, 50))
        boton_hola.clicked.connect(self.hola)
        layout = QHBoxLayout()
        layout.addWidget(boton_hola)
        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

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
