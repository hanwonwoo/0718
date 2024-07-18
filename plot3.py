#문자 메세지 길이 판별 클래스
#문제메세지 길이에 따라 문자요금 결정 프로그램 작성
#문자 메세지 길이에 따라 부과되는 요금은 클래스 생성, 속성 정보 갖게 됨
#요금이 부과될때 문자 메세지 길이 정할 수 있도록 설정
#이때 사용자로부터 문자 메세지 입력 받아 문자 요금 반환하는 코드




class MMS:
    def __init__(self,len,price1,price2):
        self.len = len
        self.price_1=price1
        self.price_2=price2
    def price(self,x):
        if len(x)>=self.len:
            print('요금은',self.price_1,'입니다.')
        else:
            print('요금은',self.price_2,'입니다.')

text=input('문자를 입력하세요')
my_mms=MMS(20,100,50)
my_mms.price(text)