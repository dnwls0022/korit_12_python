'''
field선언을 하지않앗지만 method내에 객체의 속성을 정의할수있다는 점....
이렇게 메서드를 경유하게되면 기본생성자를 통해서 객체를 생성한 다음 속성에 값을 대입해야하는과정을 거쳐야한다.

객체 생성시 기본생성자호출 -> set_info() 메서드호출

그러니 allargusconstructor에 해당되는걸 정의가능
'''
class Candy:
    def set_info(self, shape, color):
        self.shape = shape
        self.color = color

    def show_info(self):
        print(f'사탕의 모양은 {self.shape}이고 ,색깔은 {self.color}입니다.')

satang = Candy()
satang.set_info('동그라미',"갈색")
satang.show_info()

'''
속성값에 대한 제한이 따로 있지 않다면()굳이

java/js

'''
class Canday2:
    #생성자정의
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        print('사탕객체생성')
    def show_info(self):
        print(f'사탕의 모양은 {self.shape}이고 ,색깔은 {self.color}입니다.')
#객체 생성 방식에서 차이가 있다.
satang = Canday2(shape='네모',color='파랑')
satang.show_info()


'''
소멸자


'''
class sample:
    def __init__(self):
        print('소멸자생성')
    def __del__(self):
        print('인스턴스 생성')
#객체 생성
sample = sample()
print()
#객체 소멸자 호출방법
del sample
'''
지금보니 코드가 다 돌아가면 객체가 소멸되는 것 같지만 굳이 소멸자를 학습하는 이유는 각체가 생성되면 메모리 공간을 차지하기 떄문에 객체가 생성될떄마다 
그곳에서 불러나온다 하지만 특정객체가 일정코드라면 이후로 전혀 사용되지않을떄에도 이전에 메모리를 차지하기 떄문에 소멸자르 통해서 강제로 객체를 
삭제해주게 되면 메모리관리가된다.

객체의 소멸시점생성시점을 개발자가 통제하기위해서 소멸자를 쓴다...
'''

'''
지금 보니까 코드 다 돌아가면 객체가 소멸되는 것 같은데 굳이 소멸자를 학습하는 이유 -> 객체가 생성되면 메모리 공간을 차지하기 때문에 객체가 생성될 때마다 그곳에서 불려나오게 됩니다. 하지만 특정 객체가 일정 코드라인 이후로 전혀 사용되지 않을 때에도 여전히 메모리를 차지하기 때문에 소멸자를 통해서 강제로 객체를 삭제해주게 되면 메모리 관리가 된다고 볼 수 있습니다.

기본 예제

생성자를 이용해서 용량을 가진 usb 인스턴스를 만드는 프로그램을 작성하시오.

지시 사항
1. 클래스 USB를 정의할 것
2. 생성자를 정의하여 매개변수로 capacity를 받을 것
3. get_info() 메서드를 정의할 것

main 단계 코드
usb = USB(64)
usb.get_info()

실행 예
USB 객체가 생성되었습니다.
64GB USB 
'''

class USB:
    def __init__(self, capacity):
        self.capacity = capacity
        print('usb객체생성')
    def get_info(self):
        print(f'usb의 용량은 {self.capacity}입니다.')
    # 매개변수가 없어서 self.capacity를 써야한다 있으면 그냥매개변수만써도됨
usb = USB(64)
usb.get_info()

'''
1.다음과같은방법으로 man과 woman인스턴스생성
man = Person('james') name속성을 생성자에 집어넣어라
woman = Person('emily)
2. man과 woman인스턴스가 생성되면 다음과같은 메시지출력
james is born
emily is born
3. 다음과 같은 방법으로 man 인스턴스 삭제
del man'
4. 인스턴스가 삭제되면 다음과 같은 메시지출력
james is dead
'''
class Person:
    # 1. 탄생할 때 (이름 하나만 받도록 수정)
    def __init__(self, name):
        self.name = name
        print(f'{self.name} is born')  # 태어나자마자 출력!

    # 2. 사라질 때 (del 명령어를 만났을 때)
    def __del__(self):
        print(f'{self.name} is dead')  # 사라질 때 출력!
man = Person('james')
woman = Person('emily')

del man
print('위 문장에서 man객체 소멸시킴')

'''
프로그램종료시 객체들을 다 종료시킨다.
'''