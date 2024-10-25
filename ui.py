# ch 7.6.1 ui.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox)   # QLineEdit, QComboBox 추가
from PyQt5.QtGui import QIcon

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        self.btn1 = QPushButton('Calc', self)   # 버튼 이름 변경
        self.btn2 = QPushButton('Clear', self)

        self.le1 = QLineEdit('0', self) # 라인 에디터1 추가
        self.le1.setAlignment(Qt.AlignRight)    # 라인 에디트1 문자열 배치 설정
        self.le1.setFocus(True) # 포커스 설정
        self.le1.selectAll()    # 텍스트 전체 선택

        self.le2 = QLineEdit('0', self) # 라인 에디터2 추가
        self.le2.setAlignment(Qt.AlignRight)    # 라인 에디트2 문자열 배치 설정
        
        self.cb = QComboBox(self)   # 콤보 박스 추가
        self.cb.addItems(['+', '-', '*', '/', '^', '%'])  # % 연산자 추가

        hbox_formular = QHBoxLayout()   # 새로 정의한 위젯을 QHBoxLayout에 배치
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)   # hbox_formular 배치
        vbox.addLayout(hbox)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(256,256)
        self.show()

    def setDisplay(self, text):   # 함수명 변경
        self.te1.appendPlainText(text)

    def clearMessage(self):
        self.te1.clear()