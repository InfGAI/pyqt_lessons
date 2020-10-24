import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('calendar.ui', self)
        self.btn_add.clicked.connect(self.showDate)
        self.all_events = {}

    def showDate(self, date):
        date = self.cal.selectedDate()
        self.all_events[(date, self.timeEdit.time())] = self.name.text()
        print(self.all_events)
        self.refresh()

    def refresh(self):
        self.listWidget.clear()
        for i in sorted(self.all_events):
            self.listWidget.addItem(
                '{} {} {}'.format(i[0].toString(), i[1].toString(), self.all_events[i]))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
