'''
1. if 문
 - if 문은 조건이 참일때만 해당블록실행
 2. if -else문
 - 조건이 t일때  f일때
 3. if - elif- else문


'''
int = 0
isinstance()
insage = 20
# 들여쓰기 콜론 기준엔터치기
# 줄이같으면 오류
age= int(input('나이입력>>'))
if age> 20:
    print('성인')
elif age <= 20 and age >13:
    print('청소년')
else:
    print('어린이')
'''
if 조건문의 전체 형식:

if 조건식1:
    실행문1
(elif 조건식2:)
    (실행문2)
(elif 조건식3:)
    (실행문3)
(else:)
    (실행문4)            

Nested if문(중첩if문)


'''

age = 21
has_ticket = True
print(type(has_ticket))
if age > 19:
    if has_ticket:
        print('영화관 입장가능')
    else:
        print('티켓구매')
else:
    print('미성년차 출입불가')


'''
비교연산
1. ==
2. !=
3. >=
4. <=
논리연산
1. and
2. or
3. not: !와 같음 python에선 not=이런건 없고 !=는 있어서 혼란...
 
'''


