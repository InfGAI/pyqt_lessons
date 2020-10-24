import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()



    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Координаты')

        self.coords = QLabel(self)
        self.coords.setText("Координаты:None, None")
        self.coords.move(30, 30)
        self.coords.resize(100, 40)
        self.pixmap = QPixmap('car.png')
        self.image = QLabel(self)
        self.image.setText('dfghjkl')
        self.image.setPixmap(self.pixmap.scaled(30, 20))
        self.image.move(0, 0)
        self.image.resize(30, 20)
        self.show()

    def mouseMoveEvent(self, event):
        mouse_x,mouse_y=event.x(), event.y()
        self.coords.setText("Координаты:{}, {}\n".format(
            mouse_x, mouse_y)+"Координаты:{}, {}\n".format(
            self.image.x(), self.image.y()))
        #self.image.x()<mouse_x<self.image.x()+self.image.width() and \
                #self.image.y()<mouse_y<self.image.y()+self.image.height() and\
        if 0<mouse_x<self.width() and\
                0<mouse_y<self.height():
            self.image.move(mouse_x, mouse_y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())