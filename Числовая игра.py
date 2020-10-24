import sys
from random import randint
from pymorphy2 import MorphAnalyzer
from PyQt5 import QtCore
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMessageBox


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.new_game()

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
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Числовая игра')
        btn_plus = QPushButton('Увеличить', self)
        btn_plus.resize(50, 50)
        btn_plus.move(10, 50)
        btn_minus = QPushButton('Уменьшить', self)
        btn_minus.resize(50, 50)
        btn_minus.move(240, 50)
        btn_plus.clicked.connect(self.plus)
        btn_minus.clicked.connect(self.minus)
        self.lbl = QLabel(self, text='')
        self.lbl.move(0, 150)
        self.lbl.resize(300, 100)
        self.lbl.setAlignment(QtCore.Qt.AlignHCenter)
        # self.lbl.adjustSize()
        self.lbl.setFont(QFont('Arial', 50))

        self.lbl_step = QLabel(self, text='')
        self.lbl_step.move(0, 250)
        self.lbl_step.resize(300, 100)
        self.lbl_step.setAlignment(QtCore.Qt.AlignHCenter)
        # self.lbl.adjustSize()
        self.lbl_step.setFont(QFont('Arial', 20))

    def plus(self):
        self.x += self.y
        self.step -= 1
        self.lbl.setText(str(self.x))
        self.check()

    # self.lbl.adjustSize()

    def minus(self):
        self.x -= self.z
        self.step -= 1
        self.lbl.setText(str(self.x))
        self.check()

    def check(self):
        in_frase = self.hod.make_agree_with_number(self.step).word
        self.lbl_step.setText('Осталось {} {}'.format(str(self.step), in_frase))
        if self.step > 0:
            if self.x == 0:
                win = QMessageBox.question(self, 'Поздравляю! Вы выиграли!!!', 'Сыграть ещё?',
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
                if win == QMessageBox.Yes:
                    #print('Yes clicked.')
                    self.new_game()
                else:
                    #print('No clicked.')
                    self.close()

        else:
            win = QMessageBox.question(self, 'Увы! Вы проиграли!!!', 'Сыграть ещё?',
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if win == QMessageBox.Yes:
                print('Yes clicked.')
                self.new_game()
            else:
                print('No clicked.')
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
