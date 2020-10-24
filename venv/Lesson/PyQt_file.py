import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow,QFileDialog


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        self.file_name=''
        uic.loadUi('Pyqt_file.ui', self)
        self.btn_open.clicked.connect(self.open_file_and_put_in_txtBr)
        self.btnSave.clicked.connect(self.reverseText)

    def open_file_and_put_in_txtBr(self):
        filename = QFileDialog.getOpenFileName()
        self.file_name=filename[0]
        print(self.file_name)
        f = open(self.file_name, mode="r", encoding="utf8")
        lines = f.read()
        f.close()
        self.txtBrowser.setText(lines)

    def reverseText(self):
        data = self.txtBrowser.toPlainText()
        self.txtBrowser.setText(data[::-1])



 #txtBrowser.settext(

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
