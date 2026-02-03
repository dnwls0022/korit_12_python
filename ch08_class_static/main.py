'''
1. 클래스 변슈 인스턴수변수
    인스턴스 변수: 인스턴스 마다 서로 다른 값
    클래스 변수: 모든 인스턴스가 동일한 값을 지니는 변수

    인스턴스 변수 접근방식
'''
# 클래스변수
class Korean:
     country ='한국'  # 클래스변수 1
     def __init__(self,name, age, address):
         self.name = name           # 인스턴스 변수 1
         self.age = age             #  인스턴스 변수 # 2
         self.address = address     #  인스턴스 변수 # 3
#객체생성
korean = Korean('김일',21, '서울')
print(korean.name)              # 인스턴스 변수 참조
#클래스변수참조
print(korean.country)          # 객체명.클래스변수명 으로 접근 가능
print(korean.country) #클래스    # 클래스명.클래스변수명 으로 접근 가능


'''
객체명.클래스변수명을 통해서 클래스변수에 접근이 가능하긴하지만 클래스내부코드를 보기전까지는 country라는 변수가 인스턴스 변수인지 클래스변수인지 
알수있는방법이없다
                                            
클래스변슈를 확인하고자할때는 객체명.클래스변수명보다는 클래스명.클래스변수명을 통해서참조
2.클래스메서드
'''
class Korean2:
    country = '대한민국'             # 클래스 변수의 선언 및 초기화
    #클래스 메서드 정의방법
    @classmethod                  #@classmethod
    def trip(cls, trevalling_site):
        if cls.country == trevalling_site:
            print('국내여행')
        else:
            print('해외여행')
#클래스 메서드 호출
Korean2.trip('한국')
Korean2.trip('미국')
#객체 생성
person2 =Korean2()
person2.trip('일본')         #객체명.클래스메서드()호출도가능하긴함

'''
3. 정적 메서드(static method)
    self를 쓰지않는다 즉 인스턴스 변수에 접근하여 사용하는것이 불가하다. self.속성명을 사용하여 인스턴스변수의 값을 참조하는데 정적 메서드는 아에 
    첫번째 매개변수가 고정되어있지않다. 인스턴스변수를 참조하지 못한다는 점에서 클래스메서드와의 공통점에 해당

    인스턴스를 생성하지 않아도 사용가능 클래스 메서드와 공통점#2
    
    특징: 
    1) 인스턴스/클래스로 호출가능 -> 클래스 메서드와의 공통점
    2) 생성된 
    3)
    4) 반드시 작성해야하는 매개변수 (self/cls)가없다 
    
    정적 메서드는 self/cls를 둘다 사용하지않기 때문에 인스턴스클래스변수를 모두 사용하지 않는 메서드를 정의한 경우임

'''
class Korean3:
    country = '한국'

    @staticmethod
    def slogan():
        print('Imagine Your Korean! 🤖')

    @staticmethod
    def slogan2(str_example):
        print(f'Imagine Your Korean! 🤖 {str_example}')

#static mehthod호출
Korean3.slogan()
Korean3.slogan2('춥다')

'''

'''
class Bag:
    count = 0

    def __init__(self): # 여기내부나 인스턴스메서드 내부에서 self쓰면 속성이 선언된다.
        Bag.count += 1  # cls.count가 아닌 Bang.count임
                        # 즉 생성자는 인스턴스 메서드이기때문에 인스턴스 메서드 내에서 클래스 변수를 참조할 떄는 cls.클래스변수명이 아닌
                        # 클래스
        print('가방객체생성')
    @classmethod
    def sell(cls):
        print('가방이팔렷다') # cls가 잇으니 cls 위엔 cls가 없다.
        cls.count -= 1
    @classmethod
    def remain_bag(cls):
        return cls.count
#객체생성
bag1 = Bag()
print(f'현재가방재고:{Bag.count}') #인스턴스 메서드를 통해서 클래스변수의 값을 바꿨다. 모든 Bag클래스의 인스턴스들이 공유한다.
bag2 = Bag()
bag3 = Bag()
print(f'현재가방재고: {Bag.count}')
bag1.sell()                      #객체명.클래스메서드()호출  실제로 bag1이 소멸된것은아님..
print(f'현재가방재고: {Bag.count}')

'''
응용 예제
1. 다음 지시 사항을 읽고 이름과 전체 인구수를 저장할 수 있는 Person 클래스를 작성하시오.

지시 사항

1. 다음과 같은 방법으로 man과 woman 인스턴스를 생성하시오.
man = Person('김일')
woman = Person('김이')

2. man 과 woman 인스턴스가 생성되면 다음과 같은 메시지를 출력할 수 있도록 작성하시오.
김일이(가) 태어났습니다.
김이이(가) 태어났습니다.
/
3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 작성하시오.
print(f'전체 인구수 : {Person.get_population()}')

4. 다음과 같은 명령어로 man 인스턴스를 삭제하시오.
del man

5. man 인스턴스가 삭제되면 다음과 같은 메시지를 출력할 수 있도록 소멸자를 정의하시오.
RIP 김일
'''
class Person:
    # [추가] 전체 인구수를 기록할 '전광판' (클래스 변수)
    # 특정 개인의 것이 아니라 Person 클래스 전체가 공유해요.'이름'은 나만 알면 되지만, '전체 인구수'는 마을 전체가 공유해야 하는 데이터죠?
    # 그래서 self.을 붙이지 않고 클래스 바로 밑에 적어두는 거예요.
    population = 0

    def __init__(self, name):
        self.name = name
        # [추가] 사람이 태어날 때마다 전광판 숫자를 1 올립니다.
        # 모든 사람이 공통으로 쓰는 Person이라는 설계도의 전광판 숫자를 올려라!"**라는 뜻으로 Person.population
        Person.population += 1
        print(f'{self.name} 이(가) 태어났습니다.')

    def __del__(self):
        # [추가] 사람이 죽을 때(del) 전광판 숫자를 1 내립니다.
        Person.population -= 1
        # [수정] "태어났습니다"를 "RIP" 또는 "사라졌습니다"로 바꿉니다.
        print(f'RIP {self.name}')

    # [추가] 전광판 숫자를 읽어서 알려주는 '정적 메서드'
    '''
    특정 개인(self)에게 물어볼 필요가 없는 질문 정적 메서드 (Static): "관리소장님, 이 마을 전체 인구가 몇 명인가요?"
    (특정 인물이 아니라 마을 시스템에 묻는 것)
    '''
    @staticmethod
    def get_population():
        return Person.population

# --- 여기서부터는 작성하신 실행 코드 그대로! ---
man = Person('김일')
woman = Person('김이')

# 김일 삭제 (RIP 김일 출력)
del man

# 전체 인구수 조회 (김일이 떠났으니 1이 출력됨) - 전광판역할 마을이장님 ㅋㅋ static메서드사용
print(f'전체 인구수 : {Person.get_population()}')




# __init__: 객체가 태어날 때 자동으로 실행되는 함수 (생성자)

# __del__: 객체가 사라질 때 자동으로 실행되는 함수 (소멸자)


'''
언제 써야 할지 헷갈린다면?
이 질문을 스스로에게 던져보세요.

"이 기능(함수)이 돌아갈 때, 붕어빵(객체) 안에 든 팥이나 슈크림 정보가 필요한가?"

필요하다면? → 일반 메서드 (self 사용)

전혀 필요 없다면? → 정적 메서드 (@staticmethod 사용)
static메서드 호출 : 클래스이름. 변수명
'''
'''
@staticmethod 사용
get_population은 특정 개인(self)의 이름을 물어보는 게 아니라, 클래스에 저장된 전체 숫자만 딱 알려주면 되죠? 그래서 정적 메서드로 만드는 게 
가장 깔끔합니다.
'''
