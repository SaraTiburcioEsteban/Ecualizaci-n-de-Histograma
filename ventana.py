# Importar bibliotecas
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
# Instancia de la clase QApplication

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.inicializar()
    def inicializar(self):
        self.hola=QPushButton('hola')
        self.setCentralWidget(self.hola)
        self.show()
# Iniciar el ciclo de eventos

if __name__=="__main__":
    app= QApplication(sys.argv)
    window = ventana()
    sys.exit(app.exec())