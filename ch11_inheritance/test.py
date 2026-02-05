'''
지시 사항
1. 슈퍼 클래스 Shape를 정의하시오.
    - 생성자에 name을 인스턴스 변수로 설정
    - draw() 메서드를 정의하여 self.name을 출력하시오(call1() 유형)
    - area() 메서드를 정의
2. Shape 클래스를 상속 받는 서브 클래스 Circle을 정의하시오.
    - Circle은 radius(반지름) 속성을 추가로 가집니다.
    - 생성자에서 radius도 추가할 것.
    - area() 메서드를 정의하여 원의 넓이를 계산하고 return 할 것. -> call3()
        (넓이 = 3.14 * radius * radius)

3. Shape 클래스를 상속 받는 서브 클래스 Rectangle을 정의하시오.
    - Rectangle은 width(너비) / height(높이) 속성을 추가로 가집니다.
    - 생성자에서 width / height를 초기화할 것
    - area() 메서드를 정의하여 사각형의 넓이를 계산하고 return 할 것 -> call3()
        (넓이 = 너비 * 높이)

4. Circle과 Rectangle의 draw() 메서드를 오버라이딩하여 각각의 넓이를 출력할 것.

circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')

실행 예
반지름이 5인 원1이 생성되었습니다.
이름이 원1인 원의 넓이는 ____ 입니다.
원의 넓이 : ____
너비가 10, 높이가 8인 직사각형1이 생성되었습니다.
이름이 직사각형1인 직사각형의 넓이는 ____ 입니다.
직사각형의 넓이 : ____
'''