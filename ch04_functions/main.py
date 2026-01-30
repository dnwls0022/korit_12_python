'''
1. 함수종류
    1) 파이썬 내장 함수
    2) 메서드
    3) 사용자 정의 함수
2. 함수 용어
    1) 함수정의: 사용자 정의 함수를 새로 만드는 것
    2) 인수: 함수에 전달할 입력값
    3) 매개변수: argument 를 받아서 저장하는 변수
    4) 변환값/결과값/return값 : 함수의 출력값out put
    5) 함수호출: 함수를 실제로 사용하는것
3. (사용자정의 )함수 정의:
    1) 함수 정의 부분
def 함수_이름(매개변수1 매개변2)
    실행문
    return ~~~~
    2)함수호출
변수 = 함수_이름(argument1,argument2)

'''
eng_name=input('당신의 이름을 영어로입력>>>')
eng_name_up=eng_name.upper()
eng_name_low=eng_name.lower()
print(f'{eng_name_low}/{eng_name_up}')

'''
str자료형에 딸려있는 .메서드명으로 호출하는 애들이 메서드
.lower()는 str데이터를 전부 소문자로바꾸고
.upper()는 str데이터를 전부 대문자로바꾼다
특정 클래스에 종속되어있는 함수들을 메서드라고한다..........
독립적사용이가능

call1() - 그냥출력만함
call2() - 정해진게있고 그걸 거기안에서 계산만함 돌려받지않음
call3() - 매개변수가있고 그걸 거기안에서 계산만함 돌려받지않음
call4() - 매개변수가있고 그걸 거기안에서 계산함 돌려받음
유형정의        

'''
# call2 유형 매개변수있고 리턴없음
#함수정의파트
def multiply(n):
    for i in range(1,10):
        print(f'{n} x {i} = {n*i}')



dan = input("몇단을 출력하시겠습니까?>>>")

#함수호출
multiply(dan)

'''
연산자중 파이썬에만 있는
+
-
*
/
%
**
// - 몫 연산자

'''

print(5%2) # Answer: 1
print(5//2) #  Answer: 2

'''
'''

#vending_machine이라는 함수정의 money매개변수
def vending_machine(money):
    # 음료수는 초기설정 700원고정일때
    drink_price = 700
    # for money가
    for i in range(money // drink_price+1):
        print(f'음료수 = {i}개, 잔돈={money - i*drink_price}')

vending_machine(3000)