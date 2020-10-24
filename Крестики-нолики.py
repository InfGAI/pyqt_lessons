import sys
from random import randint

from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox, QRadioButton, QGridLayout
from pymorphy2 import MorphAnalyzer


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.n = 0
        self.total = [0, 0]
        self.matr = [0] * 9
        self.point = MorphAnalyzer().parse('очко')[0]
        self.initUI()
        # self.new_game()

    def initUI(self):
        self.setFixedSize(300, 300)

        self.setWindowTitle('Крестики-нолики')
        self.player1 = QRadioButton('1 игрок')
        self.player2 = QRadioButton('2 игрок')
        self.player1.resize(20, 50)
        self.player1.setFont(QFont('Arial', 15))
        self.player2.resize(20, 50)
        self.player2.setFont(QFont('Arial', 15))
        self.player1.toggled.connect(self.player)
        self.player2.toggled.connect(self.player)
        # self.player1.setChecked(True)
        self.list_btn = [QPushButton() for i in range(9)]
        grid = QGridLayout(self)
        # grid.setRowMinimumHeight(50,50)
        grid.addWidget(self.player1, 0, 0)
        grid.addWidget(self.player2, 0, 2)
        i = 1
        j = 0

        for cb in self.list_btn:
            cb.clicked.connect(self.on_click)
            cb.setMinimumHeight(75)
            # cb.setText(str((i-1)*3+j+1))
            grid.addWidget(cb, i, j)
            j = (j + 1) % 3
            if j == 0:
                i += 1

        self.setLayout(grid)

    def on_click(self):
        if self.n == 0:
            win = QMessageBox.question(self, 'Новая игра', 'Выберите игрока, для первого хода',
                                       QMessageBox.Yes)

        else:
            sender = self.sender()
            nsender = self.list_btn.index(sender)
            if self.matr[nsender] == 0:
                self.matr[nsender] = self.n
                self.check(nsender)
                if self.n == 1:
                    sender.setText('X')
                    self.n = 2
                else:
                    sender.setText('O')
                    self.n = 1

            else:
                win = QMessageBox.question(self, 'Ошибка', 'Эта клетка уже занята!',
                                           QMessageBox.Yes)

    def player(self, state):
        sender = self.sender()
        if sender == self.player1:
            self.n = 1
        else:
            self.n = 2

        print(self.n)

    def new_game(self):
        self.player1.setChecked(False)
        self.player2.setChecked(False)
        for cb in self.list_btn:
            cb.setText('')

    def check(self, nsender):
        print(self.matr)
        if (nsender in [1, 4, 7]) and (self.matr[nsender] == self.matr[nsender + 1] == self.matr[nsender - 1]) or \
                (nsender in [0, 1, 2]) and (self.matr[nsender] == self.matr[nsender + 3] == self.matr[nsender + 6]) or \
                (nsender in [6, 7, 8]) and (self.matr[nsender] == self.matr[nsender - 3] == self.matr[nsender - 6]) or \
                (nsender in [3, 4, 5]) and (self.matr[nsender] == self.matr[nsender + 3] == self.matr[nsender - 3]) or \
                (nsender in [0, 3, 6]) and (self.matr[nsender] == self.matr[nsender + 1] == self.matr[nsender + 2]) or \
                nsender == 4 and (self.matr[nsender] == self.matr[nsender + 4] == self.matr[nsender - 4]) or \
                nsender == 4 and (self.matr[nsender] == self.matr[nsender - 2] == self.matr[nsender + 2]) or \
                nsender == 0 and (self.matr[nsender] == self.matr[nsender + 4] == self.matr[nsender + 8]) or \
                nsender == 2 and (self.matr[nsender] == self.matr[nsender + 4] == self.matr[nsender + 2]) or \
                nsender == 8 and (self.matr[nsender] == self.matr[nsender - 4] == self.matr[nsender - 8]) or \
                nsender == 6 and (self.matr[nsender] == self.matr[nsender - 4] == self.matr[nsender - 2]):
            win = QMessageBox.question(self, 'Победа', 'Победил игрок ' + str(self.n),
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if win == QMessageBox.Yes:
                self.new_game()
            else:
                # print('No clicked.')
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
