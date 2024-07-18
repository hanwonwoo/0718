#사용자의 이름, 나이, 연락처
#'입력하신 이름은 ㅇㅇㅇ이며, 나이는 ㅇㅇㅇ, 그리고 연락처는 ㅇㅇㅇ-ㅇㅇㅇㅇ-ㅇㅇㅇㅇ입니다.'

class Person :
    def __init__(self, n, a, p):
        self.name = n
        self.age = a
        self.phone = p

    def print_info(self):
        print("사람 이름:",self.name,
              "\n사람 나이:",self.age,
              "\n사람 연락처:",self.phone)
my_person = Person("한원우", "27", "010-aaaa-aaaa")
my_person.print_info()



