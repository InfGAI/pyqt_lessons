# Импорт библиотеки
import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('films.ui', self)
        # Подключение к БД
        con = sqlite3.connect("films.db")
        # Создание курсора
        self.cur = con.cursor()
        self.comboBox.addItems([x[0] for x in self.readDataBase()])

        self.listWidget.addItems([x[1] for x in self.dataBase()])
    def readDataBase(self):
        return self.cur.execute("""SELECT genre FROM genres""").fetchall()

    def dataBase(self):
        # Выполнение запроса и получение всех результатов
        return  self.cur.execute("""SELECT * FROM film,genres
    WHERE film.genre_id = genres.genre_id AND genres.genre='комедия'""").fetchall()


        return result



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
con.close()
