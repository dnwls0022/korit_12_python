'''

클래스정의형식

class클래스명(파스칼 케이스):
본문(attribute / method)

객체 생성형식
객체명 = 클래스명
'''
# 클래스정의형식
class Wafflemachine:
    pass  # 클래스나 함수에 쓰면엔터쳣을떄오류

# 객체생성예시
waffle = Wafflemachine()
print(waffle)

'''
클래스 구성
1. 클래스의 기본구성
    객체를만들어내는 클래스는 객체가가여야할 구성요소를 지닌다 객체생성하기위해서 객체가할 값과기능을 지녀야함
    값 = 속성
    기능 = 메서드

    클래스를 구성하는 속성문
    1) 클래스 변수 : 클래스를 기반으로 생성된 모든 인스턴스들이 공유하는 변수 (자바에선 static변수라고부름)
    2) 인스턴스 변수 : 인스턴스들이 개별적으로 가지는 변수
    메서드는 특징에 따라서
    1) 클래스 메서드
    2) 인스턴스 메서드
    3) 정적 메서드
    
    java에선 this였는데 (아직 정의 중인 클래스에 대한 객체가 생성될수없으니 임의로 this를 썼다) python에서는 self를 쓴다
    
    self키워드 인스턴스 변수에서 각각의 객체를 의미하기 위해서 self키워드를 붙여준다.  
'''
#클래스 정의
class Person:
    def set_info(self, name, age, tel, address):
        self.name = name
        self.age = age
        self.tel = tel
        self.address = address

    def show_info(self):
        print(f'이름: {self.name}')
        print(f'나이: {self.age}')
        print(f'연락처: {self.tel}')
        print(f'주소: {self.address}')

    def show_info2(self):
        return f'제 이름은 {self.name}이고, {self.age}살 입니다. \n연락처는 {self.tel}인데, {self.address}에 살고있슴'
#객체생성
person1 = Person()
#pserson 클래스에 인스턴스에 인스턴스 메서드호출 -> 왜? 첫번째 매개변수가 self니까
person1.set_info(age=20, tel='0101010101', address='부산', name='김김')
#
person1.show_info()
print(person1.show_info2())
