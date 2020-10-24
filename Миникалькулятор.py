import sys
from random import randint

from PyQt5 import QtCore
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QMessageBox, QLineEdit


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    # self.new_game()

    def new_game(self):
        self.x = randint(1, 10)
        self.y = randint(1, 10)
        self.z = randint(1, 10)
        self.step = 10
        print(self.x, self.y, self.z)
        self.lbl.setText(str(self.x))
        self.hod = MorphAnalyzer().parse('ход')[0]
        in_frase = self.hod.make_agree_with_number(self.step).word
        self.lbl_step.setText('Осталось {} {}'.format(str(self.step), in_frase))

        # self.lbl.setText('{} {} {}'.format(str(self.x),str(self.y),str(self.z)))

    def initUI(self):
        self.setGeometry(300, 100, 300, 200)
        self.setWindowTitle('Числовая игра')
        btn_ready = QPushButton('Рассчитать', self)
        btn_ready.resize(50, 50)
        btn_ready.move(125, 75)
        btn_ready.clicked.connect(self.ready)
        self.lcd_summ = QLCDNumber(self)
        self.set_lcd(self.lcd_summ, 10, 30)
        self.lcd_minus = QLCDNumber(self)
        self.set_lcd(self.lcd_minus, 210, 30)
        self.lcd_mult = QLCDNumber(self)
        self.set_lcd(self.lcd_mult, 10, 150)
        self.lcd_div = QLCDNumber(self)
        self.set_lcd(self.lcd_div, 210, 150)
        self.lineLeft = QLineEdit(self)
        self.lineLeft.setGeometry(10, 90, 80, 20)
        self.lineRight = QLineEdit(self)
        self.lineRight.setGeometry(210, 90, 80, 20)

    def set_lcd(self, qlcd, x, y):
        qlcd.resize(80, 20)
        qlcd.setSegmentStyle(QLCDNumber.Flat)
        # get the palette
        qlcd.move(x, y)
        qlcd.setStyleSheet('''
               background-color: rgb(0, 0, 0);
               border: 2px solid rgb(113, 113, 113);
               border-width: 2px;
               color: rgb(0, 255, 0);''')
        qlcd.display(0)

    def ready(self):
        x = int(self.lineLeft.text())
        y = int(self.lineRight.text())
        self.lcd_summ.display(x + y)
        self.lcd_minus.display(x - y)
        self.lcd_mult.display(x * y)
        if y != 0:
            self.lcd_div.display(x / y)
        else:
            win = QMessageBox.question(self, 'Недопустимое значение', 'На ноль делить нельзя!',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if win == QMessageBox.Yes:
                # print('Yes clicked.')
                self.lineLeft.clear()
                self.lineRight.clear()
                self.lcd_summ.display(0)
                self.lcd_minus.display(0)
                self.lcd_mult.display(0)
                self.lcd_div.display(0)
            else:
                # print('No clicked.')
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
