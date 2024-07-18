#두 수의 덧셈, 뺄셈, 나눗셈, 곱셈 함수 만들고
#객체를 생성하시오.


class 사칙연산계산기:
        def add(self, a,b):
            result = a+b
            return result
        def mul (self, a,b):
            result = a*b
            return result
        def dev(self,a, b):
            result = a/b
            return result


app = 사칙연산계산기()
print(app.add(1,4))
