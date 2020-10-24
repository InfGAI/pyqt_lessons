import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QDialog, QInputDialog
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Главная')
        self.button1.clicked.connect(self.open_all)

    def open_all(self):
        self.hide()
        self.main_m = Main2()
        self.main_m.show()


class Main2(QMainWindow):
    def __init__(self):
        super(Main2, self).__init__()
        uic.loadUi('all.ui', self)
        self.setWindowTitle('Главная')
        self.button2.clicked.connect(self.open_all)
        self.svet.clicked.connect(self.osv)

    def osv(self):
        self.hide()
        self.main_m = Light()
        self.main_m.show()

    def open_all(self):
        self.hide()
        self.main_m = Main()
        self.main_m.show()

class Light(QDialog):
    def __init__(self):
        super(Light, self).__init__()
        uic.loadUi('light.ui', self)
        self.setWindowTitle('Освещение')

        self.Buttons.clicked.connect(self.open_main)

    def open_main(self):
        self.close()
        self.main_m = Main2()
        self.main_m.show()


class Reg(QDialog):
    def __init__(self):
        super(Reg, self).__init__()
        uic.loadUi('reg.ui', self)
        self.setWindowTitle('Вход')
        self.Buttons.clicked.connect(self.open_main)

    def open_main(self):
        self.close()
        self.main_m = Main()
        self.main_m.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Reg()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
