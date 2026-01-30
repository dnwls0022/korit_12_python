'''

1. while반복문
while다음에 나오는 조건식이 참이라면 이하의 실행문이 반복실행된다 조건이 f일때까지

형식:
while조건식1:
    반복실행문1

당연히 특정 시점에 while반복문이 종료될수 있도록 지정해주어야 한다...

1-10출략
'''

n=1
while n<=10:
    print(n, end=' /')
    n+=1  # python엔 ++가 없다.
'''
기본예제2
10-1 역순출력

'''
print() #개행
n2=10
while n2>=0:
    print(n2, end=' /')
    n2-=1

'''

'''

dan = 2
while dan<=10:  #조건문1
    number= 1
    while number <= 10:         #조건문2
        print(f'{dan} x {number} = {dan * number}') #반복실행문2
        number+=1
    dan+=1
    print()         #반복실행문1-b

    #행이 진짜진짜 중요함 다르면 인식못함 들여쓰기...귀찮네



