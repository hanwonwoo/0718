#부동산 정보 클래스 위치, 평수, 건물의 종류, 가격, 건물이 지어진 년도 정보
# 정보 확인 함수 사용
# 부동산 객체에 포함된 속성 정보를 출력

class building:
    def __init__(self, loc, y, p, a, k):
        self.location = loc
        self.year = y
        self.price = p
        self.area = a
        self.kind = k
    def print_info(self):
        print("건물 위치 :",self.location,
              "\n건물 년식 :",self.year,
              "\n건물 가격 :",self.price,
              "\n건물 평수 :",self.area,
              "\n건물 종류 :",self.kind)

my_building = building("강남","2008년","22억", "30평", "상가")
my_building.print_info()











building("강남","2008","22억","25평", "상가")

