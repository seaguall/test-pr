# ch 7.5.2 ctrl.py
class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self):    # calculate 메서드 추가, 내용은 추후에 작성
        try:    # 숫자가 아닌 값이 입력되었을 때도 프로그램이 동작하도록 예외 처리 구문 추가
            num1 = float(self.view.le1.text())      # 첫 번째 라인 에디트에 입력된 숫자를 읽어옴
            num2 = float(self.view.le2.text())      # 두 번째 라인 에이트에 입력된 숫자를 읽어옴
            operator = self.view.cb.currentText()   # 콤보 박스에 선택된 연산자 확인

            # 연산자에 따라 각각 다른 함수를 사용하여 결과를 리턴
            if operator == '+':     # 연산자가 '+'이면 덧셈 결과를 문자열로 리턴
                return f'{num1} + {num2} = {self.sum(num1, num2)}'
            elif operator == '-':
                return f'{num1} - {num2} = {self.sub(num1, num2)}'
            elif operator == '*':
                return f'{num1} * {num2} = {self.mul(num1, num2)}'
            elif operator == '/':
                return f'{num1} / {num2} = {self.div(num1, num2)}'
            elif operator == '^':
                return f'{num1} ^ {num2} = {self.pow(num1, num2)}'
            elif operator == '%':       # '%'를 입력했을 때 mod 연산 결과를 출력하도록 추가
                return f'{num1} % {num2} = {self.mod(num1, num2)}'
            else:
                return "Calculation Error"
        
        except:
            return "Calculation Error"

    def connectSignals(self):       # btn1을 클릭하면 calculate 결과가 화면에 표시되도록 수정
        self.view.btn1.clicked.connect(lambda:self.view.setDisplay(self.calculate()))    
        self.view.btn2.clicked.connect(self.view.clearMessage)

    def sum(self, a, b):    # 예외 처리 제거 : 향후 calculate 함수에서 처리하도록 구현 예정
        return a + b

    def sub(self, a, b):    # 뺄셈 추가
        return a - b

    def mul(self, a, b):    # 곱셈 추가
        return a * b

    def div(self, a, b):    # 예외 처리를 사용하도록 수정
        try:
            if (b == 0):
                raise Exception("Divisor Error")
        except Exception as e:
            return e

        return a / b

    def pow(self, a, b):    # 예외처리를 사용하도록 수정
        try:
            if (a == 0):
                raise Exception("Base Error")
        
        except Exception as e:            
            return e
        
        return pow(a, b)

    def mod(self, a, b):    # 나눗셈 연산의 나머지를 리턴하는 함수 추가
        try:
            if (b == 0):
                raise Exception("divisor Error")
        
        except Exception as e:            
            return e
        
        return a % b
        