import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QMessageBox


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('calc.ui', self)
        self.btnEq.clicked.connect(self.equal)
        self.bntFact.clicked.connect(self.fact)
        self.btnSqr.clicked.connect(self.sqr)
        self.btnSqrt.clicked.connect(self.sqrt)
        self.btnDel.clicked.connect(self.fdel)
        self.btnCe.clicked.connect(self.ce)
        self.numGroup.buttonClicked.connect(self.add_num)
        self.sign2Group.buttonClicked.connect(self.add_sign)
        self.fdel()

    def fdel(self):
        self.lineEdit.setText('')
        self.left = 0
        self.right = ''
        self.sign = '+'

    def ce(self):
        if self.lineEdit.text() != '':
            self.lineEdit.setText(self.lineEdit.text()[:-1])

    def add_num(self, btn):
        # sender = self.sender() не подходит ибо возвращает всю группу
        sender = btn
        result = self.lineEdit.text() + sender.text()
        self.lineEdit.setText(result)
        self.right += sender.text()

    def add_sign(self, btn):
        # sender = self.sender() не подходит ибо возвращает всю группу
        sender = btn
        if sender.text() == '-' and self.lineEdit.text() == '':
            self.lineEdit.setText('-')
            self.right = '-'
        elif self.lineEdit.text()[-1].isnumeric():  # проверяем, что до этого введено число
            self.right = int(self.right)
            self.left = self.calculate(self.left, self.right, self.sign)
            self.sign = sender.text()
            self.right = ''
            print(self.left, self.right, self.sign)
            # result=self.lineEdit.text()+sender.text()
            self.lineEdit.setText(str(self.left) + sender.text())

    def calculate(self, left, right, sign):
        if sign == '-':
            return left - right
        elif sign == '+':
            return left + right
        elif sign == '*':
            return left * right
        elif right != 0:
            return left / right
        else:
            return 'Error'

    def equal(self, date):
        if self.lineEdit.text()[-1].isnumeric():  # проверяем, что до этого введено число
            self.right = int(self.right)
            result = self.calculate(self.left, self.right, self.sign)
            self.lineEdit.setText(str(result))

    def sqr(self):
        if self.lineEdit.text()[-1].isnumeric():  # проверяем, что до этого введено число
            self.right = int(self.right)
            n = self.calculate(self.left, self.right, self.sign)
            result = n * n
            self.lineEdit.setText(str(result))
            self.right = result
            self.sign = '+'
            self.left = 0

    def sqrt(self):
        if self.lineEdit.text()[-1].isnumeric():  # проверяем, что до этого введено число
            self.right = int(self.right)
            n = self.calculate(self.left, self.right, self.sign)
            if n >= 0:
                result = n ** (1 / 2)
                self.lineEdit.setText(str(result))
                self.right = result
                self.sign = '+'
                self.left = 0
            else:
                win = QMessageBox.question(self, 'Ошибка', 'Невозможно извлечь  корень',
                                           QMessageBox.Yes)

    def fact(self):
        if self.lineEdit.text()[-1].isnumeric():  # проверяем, что до этого введено число
            self.right = int(self.right)
            n = self.calculate(self.left, self.right, self.sign)
            result = 1
            for i in range(2, n + 1):
                result *= i
            self.lineEdit.setText(str(result))
            self.right = result
            self.sign = '+'
            self.left = 0


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
