# DemoForm2.py
# DemoForm2.py(로직) + DemoForm2.ui(화면단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#디자인 파일을 로딩(DemoForm2)
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼클래스 정의(QMainWindow를 상속, 변경)
class DemoForm(QMainWindow, form_class):
    #생성자 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯 메서드를 추가
    def firstClick(self):
        self.label.setText("첫번째 Qt데모~~")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭~~")

#진입점 체크(Entry Point main())
#if __name__ == "__main__":
#실행프로세스 생성
app = QApplication(sys.argv)
#화면 생성
demoWindow = DemoForm()
demoWindow.show()
#이벤트 대기
app.exec_() 