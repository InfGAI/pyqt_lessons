import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Четвёртая программа')

        self.btn = QPushButton('0', self)
        self.btn.resize(100, 100)
        self.btn.move(100, 100)
        # Подпишем функцию-слот self.count() на сигнал clicked кнопки btn
        self.btn.clicked.connect(self.count)

    def count(self):
        # Не забываем, что надпись на кнопке - это текст.
        self.btn.setText(f"{int(self.btn.text()) + 1}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())