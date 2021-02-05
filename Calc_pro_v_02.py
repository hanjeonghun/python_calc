# 계산기 내부 프로그램 (괄호편)
from Calc_pro_v_01 import Calc_program_v1
from Calc_pro import Calc_program

class Calc_program_v2():

    def __init__(self, input_data_R):  # 인스턴스 메소드
        self.input_data = input_data_R # 외부에서 들어온 수식
        self.list_input_data = list(self.input_data)
        self.int_data = [] # 숫자 리스트
        self.int_refined_data = [] # 정제된 숫자 리스트
        self.str_data = [] # 문자 리스트
        self.int1 =0 # 더해진 값
        self.str_add = '' # 문자의 위치 값
        self.lead = 0
        self.open_pos = self.open_pos = self.input_data.index('(')+1
        self.open_pos_list = []
        self.close_pos = self.input_data.index(')')
        self.close_pos_list = []
        self.count = self.input_data.count('(')
        self.loop_count = 0

    def power(self):
        print('괄호 감지')
        
        while self.loop_count != self.count: # 참일 경우 반복
            
            
            for all_index, all_value in enumerate(self.input_data):
                if all_value == '(':
                    self.open_pos_list.append(all_index)
                    print('괄호 열림 위치 : ',self.open_pos_list)

                elif all_value == ')':
                    self.close_pos_list.append(all_index)
                    print('괄호 닫힘 위치 : ',self.close_pos_list)
                    self.open_pos = self.open_pos_list[-1]+1
                    self.close_pos = self.close_pos_list[0]
                    break

            for filter in self.input_data [self.open_pos:self.close_pos]: 
                print('괄호안 수식 : ',self.input_data [self.open_pos:self.close_pos])
                if filter == str(0) or filter == str(1) or filter == str(2) or filter == str(3) or filter == str(4) or filter == str(5) or filter == str(6) or filter == str(7) or filter == str(8) or filter == str(9):
                    self.int_data.insert(0,int(filter)) # 값 정수형으로 추가
                    self.lead = 0
                
                elif filter == '+' or filter == '-' or filter == '^' or filter == '*' or filter == '/' : 
                    self.str_data.append(filter) # 값 문자형으로 추가
                    self.lead = self.lead + 1

                    for index, value in enumerate(self.int_data): # 번호표를 붙여줌
                        self.int1 += value * 10 ** index # 자릿수에 맞게 곱연산을 함

                    else:
                        self.int_refined_data.append(self.int1)
                        self.int_data.clear() # 기존에 받은 값을 초기화시킴
                        self.int1 = 0

                    if self.lead >= 2 or self.input_data[0] == '+' or self.input_data[0] == '-' or self.input_data[0] == '*' or self.input_data[0] == '^' or self.input_data[0] == '/':
                        self.int_refined_data.pop()                       
                        self.str_data.pop()

            for index, value in enumerate(self.int_data): # 번호표를 붙여줌
                    self.int1 += value * 10 ** index # 자릿수에 맞게 곱연산을 함

            else:
                self.int_refined_data.append(self.int1)
                self.int_data.clear() # 기존에 받은 값을 초기화시킴
                self.int1 = 0

            while bool(len(self.int_refined_data)) == True:

                if  '^' in self.str_data :
                    self.str_add = self.str_data.index('^')
                    self.int_refined_data[self.str_add] = self.int_refined_data[self.str_add] ** self.int_refined_data[self.str_add + 1]
                    self.int_refined_data.pop(self.str_add +1)
                    self.str_data.pop(self.str_add)

                elif  '*' in self.str_data :
                    self.str_add = self.str_data.index('*')
                    self.int_refined_data[self.str_add] = self.int_refined_data[self.str_add] * self.int_refined_data[self.str_add + 1]
                    self.int_refined_data.pop(self.str_add +1)
                    self.str_data.pop(self.str_add)

                elif  '/' in self.str_data :
                    self.str_add = self.str_data.index('/')
                    self.int_refined_data[self.str_add] = self.int_refined_data[self.str_add] / self.int_refined_data[self.str_add + 1]
                    self.int_refined_data.pop(self.str_add +1)
                    self.str_data.pop(self.str_add)

                elif  '+' in self.str_data :
                    self.str_add = self.str_data.index('+')
                    self.int_refined_data[self.str_add] = self.int_refined_data[self.str_add] + self.int_refined_data[self.str_add + 1]
                    self.int_refined_data.pop(self.str_add +1)
                    self.str_data.pop(self.str_add)

                elif  '-' in self.str_data :
                    self.str_add = self.str_data.index('-')
                    self.int_refined_data[self.str_add] = self.int_refined_data[self.str_add] - self.int_refined_data[self.str_add + 1]
                    self.int_refined_data.pop(self.str_add +1)
                    self.str_data.pop(self.str_add)

                elif len(self.int_refined_data) == 1:
                    self.list_input_data[self.open_pos-1 : self.close_pos+1] = str(self.int_refined_data[0])                  
                    self.input_data = ''.join(self.list_input_data)
                    break

            print('인풋값 : ',self.input_data)        
            self.loop_count += 1
            self.int_refined_data = []
            self.list_input_data = list(self.input_data)
            self.close_pos_list.clear()
            self.open_pos_list.clear()


        program = Calc_program_v1(self.input_data)
        return program.power()

if __name__ == '__main__':
    a = Calc_program_v2(input('값을 입력해주세요 : '))     
    a.power() 