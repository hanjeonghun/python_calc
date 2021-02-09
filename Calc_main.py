import sys
from Calc_pro_bracket import Calc_program_bracket
from Calc_pro_basic import Calc_program_basic
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QApplication, QLCDNumber, QLabel, QLineEdit, QWidget, QPushButton
from PyQt5.QtCore import Qt 


class Calculator(QWidget):

    btn_x = 88
    btn_y = 60
    widget_x = 357 # 위젯 크기 (가로)
    widget_y = 555 # 위젯 크기 (세로)
    input_data = []

    def __init__(self):
        super().__init__()
        self.initUI()        

    def button_generator(self, symbol, postion_x, postion_y, hotkey):

        btn = QPushButton(symbol, self)
        btn.setGeometry(postion_x, postion_y, self.btn_x, self.btn_y)
        btn.clicked.connect(lambda :self.input_data.append(symbol))
        btn.clicked.connect(self.btn_click)
        btn.setShortcut(hotkey)
        return btn

    def special_button_generator(self, symbol, postion_x, postion_y, hotkey):
    
        btn = QPushButton(symbol, self)
        btn.setGeometry(postion_x, postion_y, self.btn_x, self.btn_y)
        btn.clicked.connect(self.btn_click)
        btn.setShortcut(hotkey)
        return btn

    def initUI(self):

# 숫자 버튼 (기호, 위치 조정, (람다식) 값 추가, 함수 연결, 단축키)
        btn0 = self.button_generator('0', 1+(self.btn_x+1)*1, self.widget_y-(self.btn_y+1)*1,"0")
        btn1 = self.button_generator('1', 1+(self.btn_x+1)*0, self.widget_y-(self.btn_y+1)*2,"1")
        btn2 = self.button_generator('2', 1+(self.btn_x+1)*1, self.widget_y-(self.btn_y+1)*2,"2")
        btn3 = self.button_generator('3', 1+(self.btn_x+1)*2, self.widget_y-(self.btn_y+1)*2,"3")
        btn4 = self.button_generator('4', 1+(self.btn_x+1)*0, self.widget_y-(self.btn_y+1)*3,"4")
        btn5 = self.button_generator('5', 1+(self.btn_x+1)*1, self.widget_y-(self.btn_y+1)*3,"5")
        btn6 = self.button_generator('6', 1+(self.btn_x+1)*2, self.widget_y-(self.btn_y+1)*3,"6")
        btn7 = self.button_generator('7', 1+(self.btn_x+1)*0, self.widget_y-(self.btn_y+1)*4,"7")
        btn8 = self.button_generator('8', 1+(self.btn_x+1)*1, self.widget_y-(self.btn_y+1)*4,"8")
        btn9 = self.button_generator('9', 1+(self.btn_x+1)*2, self.widget_y-(self.btn_y+1)*4,"9")

# 기호 버튼 (기호, 위치 조정, (람다식) 값 추가, 함수 연결, 단축키)
        btn_plus = self.button_generator('+',1+(self.btn_x+1)*3, self.widget_y-(self.btn_y+1)*2, "+")
        btn_multiply = self.button_generator('*',1+(self.btn_x+1)*3, self.widget_y-(self.btn_y+1)*4,"*")
        btn_divison = self.button_generator('/',1+(self.btn_x+1)*3, self.widget_y-(self.btn_y+1)*5,"/")
        btn_squared = self.button_generator('^',1+(self.btn_x+1)*0, self.widget_y-(self.btn_y+1)*6,"^")
        btn_bracket_open = self.button_generator('(',1+(self.btn_x+1)*0, self.widget_y-(self.btn_y+1)*5,"(")
        btn_bracket_close = self.button_generator(')',1+(self.btn_x+1)*1, self.widget_y-(self.btn_y+1)*5,")")
        btn_root = self.button_generator('√',1+(self.btn_x+1)*2, self.widget_y-(self.btn_y+1)*5,"")
        btn_enter = self.button_generator('=',1+(self.btn_x+1)*3, self.widget_y-(self.btn_y+1)*1,'')
        btn_enter.clicked.connect(self.result)
        enter = QKeySequence(Qt.Key_Return)
        btn_enter.setShortcut(enter)

# 예외 버튼 (기호, 위치 조정, 함수 연결, 단축키)
        btn_remove = self.special_button_generator('remove',1+(self.btn_x+1)*3, self.widget_y-(self.btn_y+1)*6,'backspace')
        btn_remove.clicked.connect(lambda :self.input_data.pop())

        btn_clear = self.special_button_generator('clear',1+(self.btn_x+1)*2, self.widget_y-(self.btn_y+1)*6,'ctrl+backspace')
        btn_clear.clicked.connect(lambda :self.input_data.clear())
        
        btn_minus = self.special_button_generator('-',1+(self.btn_x+1)*3, self.widget_y-(self.btn_y+1)*3,'-')
        btn_minus.clicked.connect(lambda :self.input_data.append('`'))        

# 그외..       
        btn_clear_entry = QPushButton('clear entry', self)
        btn_clear_entry.setGeometry(1+(self.btn_x+1)*1, self.widget_y-(self.btn_y+1)*6, self.btn_x, self.btn_y)
        btn_clear_entry.clicked.connect(self.clear_entry)

        btn_abs = QPushButton('abs',self) # 절대값 [미구현]
        btn_abs.setGeometry(1+(self.btn_x+1)*0, self.widget_y-(self.btn_y+1)*1, self.btn_x, self.btn_y)
        btn_abs.setEnabled(False)

        btn_dot = QPushButton('.',self) # 소수점 [미구현]
        btn_dot.setGeometry(1+(self.btn_x+1)*2, self.widget_y-(self.btn_y+1)*1, self.btn_x, self.btn_y)
        btn_dot.setEnabled(False)

# 라벨
        self.sub_output = (''.join(self.input_data))

        self.sub_display = QLineEdit(self.sub_output,self) # 수식 출력
        self.sub_display.setReadOnly(True)
        self.sub_display.setGeometry(0, 0, self.widget_x, 50)
        self.sub_display.setAlignment(Qt.AlignRight)
        self.sub_display.setStyleSheet("font-size:11pt;")

        self.result_display = QLineEdit(str(0),self) # 결과값 출력
        self.result_display.setReadOnly(True)
        self.result_display.setGeometry(0, 50, self.widget_x, 100)
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setStyleSheet("font-size:18pt;font-weight:bold;")

        self.setWindowTitle('Calc') # 위젯의 이름
        self.resize(self.widget_x, self.widget_y) # 위젯이 크기
        self.setWindowIcon(QIcon('C:\\Users\\eoehd\\Pictures\\Calc_icon.png')) # 아이콘을 조정한다.
        self.show() # 위젯을 본다.
# 함수
    def btn_click(self,input_data): # 서브값 출력
        self.sub_output = (''.join(self.input_data)) # 리스트 모음 수식 출력값
        self.test_sub_output = (''.join(self.input_data))      
        self.show_sub_output = self.sub_output.replace('`','-')#.replace('=','')
        self.sub_display.setText(self.show_sub_output) # 서브 출력값
        self.sub_display.repaint()

    def result(self,input_data): # 결과값 출력
        if '(' in self.sub_output:
            program_bracket = Calc_program_bracket(self.sub_output)
            self.result_display.setText(str(program_bracket.main()))

        elif '(' not in self.sub_output:
            program = Calc_program_basic(self.sub_output)
            self.result_display.setText(str(program.main()))
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
play = Calculator()
sys.exit(app.exec_())