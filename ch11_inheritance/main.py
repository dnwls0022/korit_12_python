#정처기 실기 자바문제 람다식 키워드질문
# 커피머신질문
'''
상속

형식:
class슈퍼클래스:
    본문

class 서브클래스(슈퍼클래스)
    본문

'''
import math


#Person클래스정의
class Person:
    #이름을받기위한 생성자정의 인스턴수변수 name
    def __init__(self, name):
        self.name = name # 전달받은 name을 이 객체의 속성(self.name)으로 저장합니다.
    #먹는 함수정의 매개변수 음식을받음
    def eat(self, food):
        #f스트링으로 이름과 음식을 받아서출력함
        print(f'{self.name} 가 {food} 을 먹습니다.')
    #커피 함수정의 음료이름매개변수로받음
    def drink(self,drink_name):
        #f스트링으로 이름과 커피를 받아서출력함
        print(f'{self.name}가 {drink_name}를 마십니다.')
#객체생성 Person이라는/  '김영'이라는값을넣어줌 그러면 1. name에 김영이들어감 왜? eat에도 감자들어감.
person1= Person('김영') # 객체를생성하면 생성자가 자동호출된다. init가 자동호출된다.괄호 안에 넣은 '김영'이라는 글자가
                        # __init__(self, name)의 name 매개변수로 쏙 전달
person1.eat('감자')
#서브클래스정의 파이썬에서는 서브클래스정의할때 부모클래스를()안에쓰고 서브클래스를 class바로 옆에쓴다
class Student(Person):
    #서브클래스만의 능력 1.2
    # 1.학생만할수있는 스터디메서드
    # 2. ******* 부모의 '드링크네임'을 재정의한것
    #서브클래스 student에서는 이름과 학교를 매개변수로 받는다 (생성자정의)
    def __init__(self,name,school):
        #부모꺼는 super()쓴다 - 부모님 방으로 가서 "이름(name) 등록하는 법 좀 알려주세요!"라고 요청
        super().__init__(name)
        #자식고유의값은 그대로쓰면되는구나(super---안쓰고 그냥 바로 self.school한다
        #1.근데 여기 자식클래스(서브클래스)에서도 name을 매개변수로했는데 왜 굳아 자식꺼안쓰고 부모꺼쓸려고 super()를 쓰는거야?
        self.school = school
        #학생만할수있는 스터디메서드
    def study(self):
        # self.name은 부모에게 물려받은 이름, self.school은 자식이 새로 만든 학교 정보입니다.
        print(f'{self.name}는 {self.school}에서 공부함')
        #******* 부모의 '드링크네임'을 재정의한것
    def drink(self, drink_name):
        # 자식만의 추가 동작: 마시기 전에 학교 이름을 먼저 출력합니다. 내 학교이름을 먼저알려줌
        print(f'{self.school}에서, ')
        #부모를 호출해서 부모의 커피를 마시는 f스트링부분을 빌려옴
        super().drink(drink_name)

#서브클래스의 객체생성 Student 설계도를 바탕으로 'potter'라는 실제 인스턴스를 만듭니다.
# '해리포터'는 부모 생성자로, '호그와트'는 자식 생성자로 전달됩니다.
potter= Student(name='해리포터', school='호그와트')
# 자식 클래스에 정의된 study 메서드를 호출합니다.
potter.study()
#부모의 메서드를 정의하는 일 없이 그대로 쓸 수 있다.
# [상속의 장점] Student 클래스에 eat을 만들지 않았지만, 부모(Person) 기능을 그대로 빌려 씁니다.
# 2. 아 그럼 부모에서 정의한생성자는 서브클래스에서 무엇이든 빌려서 쓸수있는거야? 제한없이?
# 3. potter.drink('아아') 가 해리포터가 아아를 마십니다.러 나온거는 먼저 자식클래스에서 정의한 drink가 호출되고 여기서 self.school이라고했으
# 니 객체에서정의한값 호그와트를넣어서 이야기되고 그 다음 부모로가서 해리포터가 아아를 마십니다.가 출력되는구나
potter.eat('라멘')    #부모의 메서드를 정의하는 일 없이 그대로 쓸 수 있다.
potter.drink('아아')  # 오버라이딩(부모의 드링크를 재정의했다.
'''

super()를 잘 보면 슈퍼 클래스의 생성자라고 해석가능하다. 



생성자를 호출했다면 객체가 생성되었다 볼수 있는데 그렇다면 부모 클래스의 인스턴스와 자식 클래스의 인스턴스가 있는거아닌지....
맞긴하지만 그러면 별개의 인스턴스라고 봐야하냐...

자바에서 생성자는
객체가생성될떄 호출되는 특별한메서드 리턴타입을 명시하지않음
java에서는 super()->에는 생성자/super.메서드명() 으로 super자체가 객체인경우가
있지만 python에서는 super로 일원화되어있다.

즉, 이상의 코드에서 student생성자의 호출이 완벽하게 마무리된다면 super

순서는 부모먼저호출

2. 서브클래스의 인스턴스 자료형
   슈퍼 클래스의 객체는 슈퍼 클래스의 인스턴스
   서브 클래스의 인스턴스는 서브 클래스의 인스턴스이면서 동시에 슈퍼 클래스의 인스턴스(부모생성자 호출)
   
   student 클래스의 객체는 student의 인스턴스이면서  Person의 인스턴스
   
   java를 기준으로 instanceof연산자 역할을 하는 것이 js에서는 typeof연산자가 있는데 python에서는 isinstance()함수가 있다 다 소문자..
   
   형식:
   isinstance()
'''
print(isinstance(potter,Student)) #결과값 트루 (a,b) a가 b에 있는 객체이지?
print(isinstance(potter,Person)) #결과값 트루
print(isinstance(person1,Student)) #결과값FALSE

print(isinstance(person1,Person))#결과값 트루
print(issubclass(Student,Person)) #결과값 트루 객체안만들고 클래스간의 위계만 확인하고싶을떄 쓸 수 있다. Person의 자식설계도이다.

'''
3. 다음 지시 사항을 읽고 Hybrid 클래스를 구현하시오.지시사항밑에
1. 다음과 같은 슈퍼 클래스 Car를 가지고 있는 Hybrid 클래스를 구현하시오.
2. 서브 클래스 Hybrid는 다음과 같은 특징을 지니고 있습니다.
    1) 최대 배터리 충전량은 30 
    2) 배터리를 충전하는 charge() 메서드가 존재합니다. 최대 충전량을 초과할 수 없고,
        0보다 작은 값으로 충전할 수 없습니다.
    3) 현재 주유량과 충전량을 모두 확인할 수 있는 hybrid_info() 메서드가 있습니다.    -재정의? 
3. 다음과 같은 방식으로 전체 동작을 확인할 수 있습니다.
car = Hybrid(oil= 0, amount= 0) amount배터리
전기량
car.add_oil(100)

전기요금 car.charge(50)
car.hybrid_info()

실행 예
하이브리드 차량이 생산되었습니다.
기름을 50 주유 했습니다.
전기를 30 충전 했습니다.
현재 주유 상태 : 50
현재 충전 상태 : 30
'''
class Car:
    max_oil = 50
    def __init__(self,oil):
        self.oil = oil

    def add_oil(self,oil):
        if oil <= 0:
            return
        self.oil = oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil
        print(f'기름을 {self.oil} 주유 했습니다.')

    def car_info(self):
        print(f'현재 주유 상태 : {self.oil}')
#서브클래스 생성
class Hybrid(Car):
    #최대배터리 충전량 설정
    max_bettery = 30

    #부모의 오일, 새로운 amount등록
    def __init__(self,oil,amount):
        super().__init__(oil)
        self.amount = amount
        print('하이브리드 차량이 생산되었습니다.')
    #amount배터리  Hybrid.max_bettery:

    def charge(self,amount):
        if amount <= 0:
            return
        self.amount += amount
        if self.amount > Hybrid.max_bettery:
            self.amount = Hybrid.max_bettery
        print(f'전기를 {self.amount} 충전했습니다.')

    def hybrid_info(self):
        super().car_info()  #현재주유상태가 불러와짐... ->어차피 부모객체가 생성되어서 super()키워드를 통해 메서드를 호출할수 있다.
        print( f'현재 충전 상태 : {self.amount}')

car = Hybrid(oil= 0, amount= 0)
#print 현재충전상태를 보여주는건 초기에는 0으로줬고 주유하고 충전한뒤에 보여줘야하니 charge에 print쓰기
car.add_oil(100)
car.charge(50)
car.hybrid_info()
'''
원 문제
'''
class Shape:
    def __init__(self,name):
        self.name = name

    def draw(self):
        print(f'모양은{self.name}입니다')



class Circle(Shape):
    def __init__(self,name,radius):
        super().__init__(name)
        self.radius = (radius)
        print(f'반지름이{self.radius}인 {self.name}이 생성되었습니다.')
    def area(self):
        #call3유형 매개변수X, 리턴O (계산 결과만 전달)
        result = 3.14 * self.radius * self.radius
        return result
    def draw(self):
        print(f'이름이 {self.name}인  원의 넓이는 {self.area()}입니다')


class Rectangle(Shape):
    def __init__(self,name,height,width):
        super().__init__(name)
        self.height = height
        self.width = width
        print(f'너비가{self.height}인 높이{self.width}이 {self.name}이 생성되었습니다.')
    def area(self):
        #width(너비) / height(높이)
        result = (self.height * self.width)
        return result
    def draw(self):
        print(f'이름이 {self.name}인  직사각형의 넓이는 {self.area()}입니다')

circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')
