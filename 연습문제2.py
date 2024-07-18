#게임 캐릭터 만들기
#게임 캐릭터 아이디, 성별, 직업 정보
#기본 공격 함수
#기본 공격 사용 시 '공격!'화면에 출력

class Game_Char:
    def __init__ (self, n, s, j):
        self.game_id = n
        self.game_sex= s
        self.game_job= j
    def attack(self, 상대방_id, 상대방_id2):
        print(self. game_id,"(이)가", 상대방_id, 상대방_id2, "을 공격했다")

my_char= Game_Char("asd", "남", "전사")
my_char.attack("짱짱보스","asdfasdf")
