import sys
from random import randint

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox, QCheckBox,QGridLayout
from pymorphy2 import MorphAnalyzer


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.new_order()
        self.rub = MorphAnalyzer().parse('рубль')[0]

    def initUI(self):
        self.setGeometry(200, 100, 300, 300)
        self.setWindowTitle('Ваш заказ')
        btn_order = QPushButton('Заказать', self)
        btn_order.resize(50, 50)
        btn_order.move(240, 240)

        btn_order.clicked.connect(self.check)

        self.lbl = QLabel(self, text='Вас приветствует служба\n автоматического заказа.\n Выберите позиции из меню:')
        self.lbl.move(0, 10)
        self.lbl.resize(300, 100)
        self.lbl.setAlignment(QtCore.Qt.AlignHCenter)
        self.lbl.setFont(QFont('Arial', 15))
        menu = ['гамбургер', 'чизбергер', 'картошка', 'кола']
        self.price = ['50', '60', '30', '20']
        self.total = 0
        self.list_checkBox = [QCheckBox(m + '\n' + p, self) for m, p in zip(menu, self.price)]
        '''i = 10
        j = 80
        for cb in self.list_checkBox:
            cb.move(i, j)
            cb.stateChanged.connect(self.changeTotal)
            i += 80'''
        grid = QGridLayout()
        i=0
        j = 0

        for cb in self.list_checkBox:
            grid.addWidget(cb, i, j)
            cb.stateChanged.connect(self.changeTotal)
            j=(j+1)%4
            if j==0:
                i+=1

        self.setLayout(grid)

    def changeTotal(self, state):
        sender = self.sender()
        n = self.list_checkBox.index(sender)
        if state == QtCore.Qt.Checked:
            self.total += int(self.price[n])
        else:
            self.total -= int(self.price[n])
        print(self.total)

    def new_order(self):
        for cb in self.list_checkBox:
            cb.setChecked(False)

    def check(self):
        if self.total > 0:

            in_frase = self.rub.make_agree_with_number(self.total).word
            string = 'Сумма вашего заказа: {} {}'.format(str(self.total), in_frase)
            win = QMessageBox.question(self, 'Заказ', string + '\nОформить новый заказ?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if win == QMessageBox.Yes:
                # print('Yes clicked.')
                self.new_order()
            else:
                # print('No clicked.')
                self.close()
        else:
            win = QMessageBox.question(self, 'Заказ', 'Выберите интересующие позиции меню.',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if win == QMessageBox.Yes:
                # print('Yes clicked.')
                self.new_order()
            else:
                # print('No clicked.')
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
