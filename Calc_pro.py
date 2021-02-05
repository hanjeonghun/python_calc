# 계산기 내부 프로그램

class Calc_program():
    
    def __init__(self, input_data_R):  # 인스턴스 메소드
        self.input_data = input_data_R # 외부에서 들어온 수식
        self.int_data = [] # 숫자 리스트
        self.int_refined_data = [] # 정제된 숫자 리스트
        self.str_data = [] # 문자 리스트
        self.int1 =0 # 더해진 값
        self.str_add = '' # 문자의 위치 값
        self.lead = 0


    def power(self):
        for filter in self.input_data:
            if filter == str(0) or filter == str(1) or filter == str(2) or filter == str(3) or filter == str(4) or filter == str(5) or filter == str(6) or filter == str(7) or filter == str(8) or filter == str(9):
                self.int_data.insert(0,int(filter)) # 값 정수형으로 추가
                self.lead = 0
            
            elif filter == '+' or filter == '-' or filter == '^' or filter == '*' or filter == '/':
                self.str_data.append(filter) # 값 문자형으로 추가
                self.lead = self.lead + 1
                print(self.str_data)

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

        print('정제된 숫자에 값을 추가함',self.int_refined_data)
        print('문자형 리스트 ',self.str_data)
        while bool(len(self.int_refined_data)) == True: # 값이 남아있으면

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
                print("계산된 값 - ", self.int_refined_data[0])
                break

        return self.int_refined_data[0]

if __name__ == '__main__':
    a = Calc_program(input('값을 입력해주세요 : '))     
    a.power() 