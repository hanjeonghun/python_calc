class Calc_program_basic():
    
    def __init__(self, input_data):
        self.input_data = input_data
        self.int_data = [] 
        self.int_refined_data = [] 
        self.str_data = [] 
        self.int_add = 0 
        self.str_position = 0
        self.str_check = 0

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

    def main(self):
        print('입력값 : ', self.input_data)
        for filter in self.input_data:
            if filter == str(0) or filter == str(1) or filter == str(2) or filter == str(3) or filter == str(4) or filter == str(5) or filter == str(6) or filter == str(7) or filter == str(8) or filter == str(9):
                self.int_data.insert(0,int(filter)) # 값 정수형으로 추가
                self.str_check = 0
            
            elif filter == '+' or filter == '√' or filter == '`' or filter == '=' or filter == '^' or filter == '*' or filter == '/':
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

        while bool(len(self.int_refined_data)) == True: # 값이 남아있으면

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
                print("계산된 값 : ", self.int_refined_data[0])
                break

        return self.int_refined_data[0]

if __name__ == '__main__':
    a = Calc_program_basic(input('값을 입력해주세요 : '))     
    a.main() 