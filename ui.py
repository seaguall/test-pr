# ch 6.6.1 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout, QLineEdit, QComboBox)   # QLineEdit, QComboBox 추가
from PyQt5.QtGui import QIcon   # icon을 추가하기 위한 라이브러리
from PyQt5 import QtCore        # 모듈 추가

class View(QWidget):  # QWidget 클래스를 상속받아서 클래스를 정리

    def __init__(self):
        super().__init__()  # 부모 클래스 QWidget을 초기화
        self.initUI()       # 나머지 초기화는 initUI 함수에 정의

    def initUI(self):
        self.te1 = QPlainTextEdit()     # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True)      # 텍스트 에디트 위젯을 읽기만 가능하도록 수정

        self.le1 = QLineEdit('0', self)     # 라인 에디터1 추가
        self.le1.setAlignment(QtCore.Qt.AlignRight)     # 라인 에디터1 문자열 배치 설정
        self.le1.setFocus(True)     # 포커스 설정
        self.le1.selectAll()        # 텍스트 전체 선택

        self.le2 = QLineEdit('0', self)     # 라인 에디터2 추가
        self.le2.setAlignment(QtCore.Qt.AlignRight)     # 라인 에디터2 문자열 배치 설정

        self.cb = QComboBox(self)               # 콤보 박스 추가
        self.cb.addItems(['+', '-', '*', '/', '^', '%'])  # % 연산자 추가

        hbox_formular = QHBoxLayout()       # 새로 정의한 위젯을 QHBoxLayout에 배치
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        self.btn1 = QPushButton('Calc', self)       # 버튼 이름 변경
        self.btn2 = QPushButton('Clear', self)      # 버튼 2 추가

        hbox = QHBoxLayout()    # 수평 박스 레이아웃을 추가하고 버튼 1, 2 추가
        hbox.addStretch(1)      # 공백
        hbox.addWidget(self.btn1)   # 버튼 1 배치
        hbox.addWidget(self.btn2)   # 버튼 2 배치
        
        vbox = QVBoxLayout()            # 수직 레이아웃 위젯 생성
        vbox.addWidget(self.te1)        # 수직 레이아웃에 텍스트 에디트 위젯 추가
        vbox.addLayout(hbox_formular)   # hbox_formular 배치
        vbox.addLayout(hbox)            # btn1 위치에 hbox를 배치
        vbox.addStretch(1)              # 빈 공간

        self.setLayout(vbox)    # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된 레이아웃 설정

        self.setWindowTitle('Calculator')   # 윈도우에 표시되는 타이틀
        self.setWindowIcon(QIcon('icon.png'))   # 윈도우 아이콘 추가
        self.resize(256,256)    # 윈도우 사이즈
        self.show()             # 윈도우 화면이 표시되도록 설정
    
    def setDisplay(self, text):   # 함수명 변경
        self.te1.appendPlainText(text)

    def clearMessage(self):     # 버튼 2 핸들러 함수 정의
        self.te1.clear()