from Calc_pro_basic import Calc_program_basic

class Calc_program_bracket():

    def __init__(self, input_data):  # 인스턴스 메소드
        self.input_data = input_data # 외부에서 들어온 수식
        self.list_input_data = list(self.input_data)
        self.int_data = [] # 숫자 리스트
        self.int_refined_data = [] # 정제된 숫자 리스트
        self.str_data = [] # 문자 리스트
        self.int_add = 0 # 더해진 값
        self.str_positon = 0 # 문자의 위치 값
        self.str_check = 0
        self.open_position = self.open_position = self.input_data.index('(')+1
        self.open_position_list = []
        self.close_position = self.input_data.index(')')
        self.close_position_list = []
        self.close_bracket_count = self.input_data.count('(')
        self.loop_count = 0
    
    def  four_arithmetic_operations(self,symbol):
        self.str_position = self.str_data.index(symbol)
        if self.input_data[self.input_data.find(symbol)+1:self.input_data.find(symbol)+2] == '`': #symbol 다음 문자가 -일 경우 음수로 변환
            self.int_refined_data[self.str_position + 1] = self.int_refined_data[self.str_position + 1] * -1          
        if symbol == '^':
            self.int_refined_data[self.str_position] = self.int_refined_data[self.str_position] ** self.int_refined_data[self.str_position + 1]
        if symbol == '*':    
            self.int_refined_data[self.str_position] = self.int_refined_data[self.str_position] * self.int_refined_data[self.str_position + 1]
        if symbol == '/':    
            self.int_refined_data[self.str_position] = self.int_refined_data[self.str_position] / self.int_refined_data[self.str_position + 1]
        if symbol == '+':    
            self.int_refined_data[self.str_position] = self.int_refined_data[self.str_position] + self.int_refined_data[self.str_position + 1]
        if symbol == '`':
            self.int_refined_data[self.str_position] = self.int_refined_data[self.str_position] - self.int_refined_data[self.str_position + 1]       
        self.int_refined_data.pop(self.str_position +1)
        self.str_data.pop(self.str_position)

# main
    def main(self):
        print('입력값 : ', self.input_data)
        
        while self.loop_count != self.close_bracket_count: # 참일 경우 반복
  
            for all_index, all_value in enumerate(self.input_data):
                if all_value == '(':
                    self.open_position_list.append(all_index)

                elif all_value == ')':
                    self.close_position_list.append(all_index)                
                    self.open_position = self.open_position_list[-1] + 1
                    self.close_position = self.close_position_list[0]
                    break

            for filter in self.input_data [self.open_position:self.close_position+1]: 
                print('출력할 괄호안 계산 값 : ', self.input_data [self.open_position:self.close_position+1])
                if filter == str(0) or filter == str(1) or filter == str(2) or filter == str(3) or filter == str(4) or filter == str(5) or filter == str(6) or filter == str(7) or filter == str(8) or filter == str(9):
                    self.int_data.insert(0,int(filter)) # 값 정수형으로 추가
                    self.str_check = 0
                
                elif filter == '+' or filter == '√' or filter == '`' or filter == ')' or filter == '^' or filter == '*' or filter == '/':
                    self.str_data.append(filter) # 값 문자형으로 추가
                    self.str_check = self.str_check + 1

                    for index, value in enumerate(self.int_data): # 번호표를 붙여줌
                        self.int_add += value * 10 ** index # 자릿수에 맞게 곱연산을 함

                    else:
                        self.int_refined_data.append(self.int_add)
                        self.int_data.clear() # 기존에 받은 값을 초기화시킴
                        self.int_add = 0

                    if self.str_check >= 2 or self.input_data[0] == '+' or self.input_data[0] == '*' or self.input_data[0] == '^' or self.input_data[0] == '/':
                        self.int_refined_data.pop()                   
                        if self.str_data[-2] != '√':
                            self.str_data.pop()
                
                    elif self.input_data[0] == '`':
                        self.int_data.insert(0,int(0))

            print('정수 모음 : ',self.int_refined_data)
            print('문자 모음 : ',self.str_data)
            while bool(len(self.int_refined_data)) == True:   
                
                if  '^' in self.str_data :
                    self.four_arithmetic_operations('^')

                elif  '√' in self.str_data : # 200+ 200√ - 400
                    self.str_position = self.str_data.index('√')
                    self.int_refined_data[self.str_position] = self.int_refined_data[self.str_position] ** 0.5
                    self.str_data.pop(self.str_position)

                elif  '=' in self.str_data :
                    self.str_position = self.str_data.index('=')
                    self.str_data.pop(self.str_position)

                elif  '*' in self.str_data :
                    self.four_arithmetic_operations('*')

                elif  '/' in self.str_data :
                    self.four_arithmetic_operations('/')

                elif  '`' in self.str_data :
                    self.four_arithmetic_operations('`')

                elif  '+' in self.str_data :
                    self.four_arithmetic_operations('+')

                elif len(self.int_refined_data) == 1:
                    self.list_input_data[self.open_position-1 : self.close_position+1] = str(self.int_refined_data[0])                  
                    self.input_data = ''.join(self.list_input_data)
                    break

       
            self.loop_count += 1
            self.int_refined_data = []
            self.list_input_data = list(self.input_data)
            self.close_position_list.clear()
            self.open_position_list.clear()

        program = Calc_program_basic(self.input_data.replace("-",'`'))
        return program.main()

if __name__ == '__main__':
    a = Calc_program_bracket(input('값을 입력해주세요 : '))     
    a.main() 