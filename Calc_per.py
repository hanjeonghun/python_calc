import sys
import Calc_pro
from Calc_pro_v_02 import Calc_program_v2
from Calc_pro_v_01 import Calc_program_v1
from PyQt5.QtGui import QIcon,QKeySequence
from PyQt5.QtWidgets import QApplication, QLCDNumber, QLabel, QLineEdit, QWidget, QPushButton
from PyQt5.QtCore import Qt 


class MyApp(QWidget):

    
    input_data = []

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        widget_x = 357 # 위젯 크기 (가로)
        widget_y = 555 # 위젯 크기 (세로)
        btn_x = 88 # 버튼 크기 (가로)
        btn_y = 60 # 버큰 크기 (세로)
# 1층
        btn_abs = QPushButton('abs',self) # 절대값
        btn_abs.setGeometry(1+(btn_x+1)*0, widget_y-(btn_y+1)*1, btn_x, btn_y)
        btn_abs.setEnabled(False)

        btn0 = QPushButton('0', self) # 버튼 0
        btn0.setGeometry(1+(btn_x+1)*1, widget_y-(btn_y+1)*1, btn_x, btn_y)
        btn0.clicked.connect(lambda :self.input_data.append(str(0)))
        btn0.clicked.connect(self.btn_click)
        btn0.setShortcut("0")

        btn_dot = QPushButton('.',self) # 버튼 소수점
        btn_dot.setGeometry(1+(btn_x+1)*2, widget_y-(btn_y+1)*1, btn_x, btn_y)
        btn_dot.setEnabled(False)

        btn_equal = QPushButton('=',self) # 버튼 [엔터]
        btn_equal.setGeometry(1+(btn_x+1)*3, widget_y-(btn_y+1)*1, btn_x, btn_y)
        btn_equal.clicked.connect(self.result)
        enter = QKeySequence(Qt.Key_Return)
        btn_equal.setShortcut(enter)
# 2층
        btn1 = QPushButton('1', self) # 버튼 1
        btn1.setGeometry(1+(btn_x+1)*0, widget_y-(btn_y+1)*2, btn_x, btn_y)
        btn1.clicked.connect(lambda :self.input_data.append(str(1)))
        btn1.clicked.connect(self.btn_click)
        btn1.setShortcut("1")

        btn2 = QPushButton('2', self) # 버튼 2
        btn2.setGeometry(1+(btn_x+1)*1, widget_y-(btn_y+1)*2, btn_x, btn_y)
        btn2.clicked.connect(lambda :self.input_data.append(str(2)))
        btn2.clicked.connect(self.btn_click)
        btn2.setShortcut("2")

        btn3 = QPushButton('3', self) # 버튼 3
        btn3.setGeometry(1+(btn_x+1)*2, widget_y-(btn_y+1)*2, btn_x, btn_y)
        btn3.clicked.connect(lambda :self.input_data.append(str(3)))
        btn3.clicked.connect(self.btn_click)
        btn3.setShortcut("3")

        btn_plus = QPushButton('+', self) # 버튼 더하기
        btn_plus.setGeometry(1+(btn_x+1)*3, widget_y-(btn_y+1)*2, btn_x, btn_y)
        btn_plus.clicked.connect(lambda :self.input_data.append('+'))
        btn_plus.clicked.connect(self.btn_click)
        btn_plus.setShortcut("shift+=")
# 3층

        btn4 = QPushButton('4', self) # 버튼 4
        btn4.setGeometry(1+(btn_x+1)*0, widget_y-(btn_y+1)*3, btn_x, btn_y)
        btn4.clicked.connect(lambda :self.input_data.append((str(4))))
        btn4.clicked.connect(self.btn_click)
        btn4.setShortcut("4")

        btn5 = QPushButton('5', self) # 버튼 5
        btn5.setGeometry(1+(btn_x+1)*1, widget_y-(btn_y+1)*3, btn_x, btn_y)
        btn5.clicked.connect(lambda :self.input_data.append(str(5)))
        btn5.clicked.connect(self.btn_click)
        btn5.setShortcut("5")

        btn6 = QPushButton('6', self) # 버튼 6
        btn6.setGeometry(1+(btn_x+1)*2, widget_y-(btn_y+1)*3, btn_x, btn_y)
        btn6.clicked.connect(lambda :self.input_data.append(str(6)))
        btn6.clicked.connect(self.btn_click)
        btn6.setShortcut("6")

        btn_min = QPushButton('-', self) # 버튼 빼기
        btn_min.setGeometry(1+(btn_x+1)*3, widget_y-(btn_y+1)*3, btn_x, btn_y)
        btn_min.clicked.connect(lambda :self.input_data.append('-'))
        btn_min.clicked.connect(self.btn_click)
        btn_min.setShortcut("-")
# 4층
        btn7 = QPushButton('7', self) # 버튼 7
        btn7.setGeometry(1+(btn_x+1)*0, widget_y-(btn_y+1)*4, btn_x, btn_y)
        btn7.clicked.connect(lambda :self.input_data.append(str(7)))
        btn7.clicked.connect(self.btn_click)
        btn7.setShortcut("7")

        btn8 = QPushButton('8', self) # 버튼 8
        btn8.setGeometry(1+(btn_x+1)*1, widget_y-(btn_y+1)*4, btn_x, btn_y)
        btn8.clicked.connect(lambda :self.input_data.append(str(8)))
        btn8.clicked.connect(self.btn_click)
        btn8.setShortcut("8")

        btn9 = QPushButton('9', self) # 버튼 9
        btn9.setGeometry(1+(btn_x+1)*2, widget_y-(btn_y+1)*4, btn_x, btn_y)
        btn9.clicked.connect(lambda :self.input_data.append(str(9)))
        btn9.clicked.connect(self.btn_click)
        btn9.setShortcut("9")

        btn_multip = QPushButton('*',self) # 버튼 곱하기
        btn_multip.setGeometry(1+(btn_x+1)*3, widget_y-(btn_y+1)*4, btn_x, btn_y)
        btn_multip.clicked.connect(lambda :self.input_data.append('*'))
        btn_multip.clicked.connect(self.btn_click)
        btn_multip.setShortcut("shift+8")
# 5층
        btn_bracket_open = QPushButton('(', self) # 버튼 null
        btn_bracket_open.setGeometry(1+(btn_x+1)*0, widget_y-(btn_y+1)*5, btn_x, btn_y)
        btn_bracket_open.clicked.connect(lambda :self.input_data.append('('))
        btn_bracket_open.clicked.connect(self.btn_click)
        btn_bracket_open.setShortcut("shift+9")

        btn_bracket_close = QPushButton(')', self) # 버튼 null
        btn_bracket_close.setGeometry(1+(btn_x+1)*1, widget_y-(btn_y+1)*5, btn_x, btn_y)
        btn_bracket_close.clicked.connect(lambda :self.input_data.append(')'))
        btn_bracket_close.clicked.connect(self.btn_click)
        btn_bracket_close.setShortcut("shift+0")

        btn_root = QPushButton('√x', self) # 버튼 null
        btn_root.setGeometry(1+(btn_x+1)*2, widget_y-(btn_y+1)*5, btn_x, btn_y)
        btn_root.clicked.connect(self.btn_click)


        btn_divison = QPushButton('/',self) # 버튼 나누기
        btn_divison.setGeometry(1+(btn_x+1)*3, widget_y-(btn_y+1)*5, btn_x, btn_y)
        btn_divison.clicked.connect(lambda :self.input_data.append('/'))
        btn_divison.clicked.connect(self.btn_click)
        btn_divison.setShortcut("/")
# 6층
        btn_squared = QPushButton('^', self) # 버튼 제곱
        btn_squared.setGeometry(1+(btn_x+1)*0, widget_y-(btn_y+1)*6, btn_x, btn_y)
        btn_squared.clicked.connect(lambda :self.input_data.append('^'))
        btn_squared.clicked.connect(self.btn_click)
        btn_squared.setShortcut("shift+6")

        btn_clear_entry = QPushButton('clear entry', self) # 버튼 null
        btn_clear_entry.setGeometry(1+(btn_x+1)*1, widget_y-(btn_y+1)*6, btn_x, btn_y)
        btn_clear_entry.clicked.connect(self.clear_entry)

        btn_clear = QPushButton('clear', self) # 버튼 null
        btn_clear.setGeometry(1+(btn_x+1)*2, widget_y-(btn_y+1)*6, btn_x, btn_y)
        btn_clear.clicked.connect(lambda :self.input_data.clear())
        btn_clear.clicked.connect(self.btn_click)

        btn_remove = QPushButton('지우기',self) # 버튼 지우기
        btn_remove.setGeometry(1+(btn_x+1)*3, widget_y-(btn_y+1)*6, btn_x, btn_y)
        btn_remove.clicked.connect(lambda :self.input_data.pop())
        btn_remove.clicked.connect(self.btn_click)
        btn_remove.setShortcut("backspace")
# 라벨
        self.sub_output = (''.join(self.input_data))

        self.sub_display = QLineEdit(self.sub_output,self) # 수식 출력
        self.sub_display.setReadOnly(True)
        self.sub_display.setGeometry(0, 0, widget_x, 50)
        self.sub_display.setAlignment(Qt.AlignRight)
        self.sub_display.setStyleSheet("font-size:11pt;")

        self.result_display = QLineEdit(str(0),self) # 결과값 출력
        self.result_display.setReadOnly(True)
        self.result_display.setGeometry(0, 50, widget_x, 100)
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setStyleSheet("font-size:18pt;font-weight:bold;")

        self.setWindowTitle('Calc') # 위젯의 이름
        self.resize(widget_x, widget_y) # 위젯이 크기
        self.setWindowIcon(QIcon('C:\\Users\\eoehd\\Pictures\\Calc_icon.png')) # 아이콘을 조정한다.
        self.show() # 위젯을 본다.

    def btn_click(self,input_data): # 서브값 출력
        self.sub_output = (''.join(self.input_data)) # 리스트 모음 수식 출력값
        self.sub_display.setText(self.sub_output) # 서브 출력값
        self.sub_display.repaint()

    def result(self,input_data): # 결과값 출력
        if '(' in self.sub_output:
            program_v2 = Calc_program_v2(self.sub_output)
            self.result_display.setText(str(program_v2.power()))

        elif '(' not in self.sub_output:
            program = Calc_program_v1(self.sub_output)
            self.result_display.setText(str(program.power()))
        self.result_display.repaint()


    def clear_entry(self, input_data):
        print(self.input_data)
        while True:
            if self.input_data[-1] == str(0) or self.input_data[-1] == str(1) or self.input_data[-1] == str(2) or self.input_data[-1] == str(3) or self.input_data[-1] == str(4) or self.input_data[-1] == str(5) or self.input_data[-1] == str(6) or self.input_data[-1] == str(7) or self.input_data[-1] == str(8) or self.input_data[-1] == str(9):
                self.input_data.pop()
            
            elif self.input_data[-1] == '+' or self.input_data[-1] == '-' or self.input_data[-1] == '^' or self.input_data[-1] == '*' or self.input_data[-1] == '/' :
               self.sub_output = (''.join(self.input_data)) # 리스트 모음 수식 출력값
               self.sub_display.setText(self.sub_output) # 서브 출력값
               self.sub_display.repaint()
               break
    

        self.sub_display.repaint()           
        self.result_display.repaint()

                        



app = QApplication(sys.argv)
ex = MyApp()
sys.exit(app.exec_())
