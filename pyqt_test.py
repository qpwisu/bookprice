from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
import re
from openpyxl import load_workbook
import pandas as pd
import sys
from PyQt5.QtWidgets import *

class MyWindow(QWidget):

    def __init__(self):
        fname = ""
        super().__init__()
        self.setGeometry(100, 100, 800, 500)
        self.pushButton1= QPushButton("파일찾기")
        self.pushButton1.clicked.connect(self.pushButtonClicked)

        self.label = QLabel()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.pushButton1)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def pushButtonClicked(self):
        global fname
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')
        self.label.setText(fname[0])
        self.xlsx = pd.read_excel(""+fname[0])
        self.tablewidget = QTableWidget(self)
        self.tablewidget.resize(400, 400)
        self.tablewidget.setRowCount(3) # 행 개수
        self.tablewidget.setColumnCount(3) # 열 개수
        self.layout.addWidget(self.tablewidget)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()


