'''

for반복문 :
원래 python에서 default for의 경우 enhanced for가 기본이다.
index를 다루는것부터 시작...

range()
'''
# 1-100출력

for i in range(10):
    print(i+1)

'''
i가 0부터 시작한다.
range() 몇번반복할것인가를 지정
for와 연계하여 쓰인다.

range() 함수의응용
range((시작값), 한계값, (증감값))

시작값 : 생략가능, 생략하면 0부터시작
한계값 : 명시 x끝까지진행
증감값 : 생략가능 생략경우 1씩증가
'''
for i in range(2,11,2):   # 는 짝수출력  1은 홀수출력
    print(i, end=' / ')  #1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9 / 10 /

print()
print(i)  #결과값 10

'''
java에서는 for(int i =0)....하고sout하고 출력하면 오류나지만 
while과마찬가지로 지역변수의 범위가 다르다른점확인

시작값/한계값/증감값을 정의하게되는 range()함수가 필수

하지만 default의 형태로 python for - loop의 경우
'''
nums = [1,2,3,4,5]
for num in nums:
    print(i, end=' / ')
if 5 in nums:
    print('5가 nums리스트에 있습니다.')
else:
    print('5가 없습니다.')

'''
in이라는 친구가 생각보다 중요 in이 적용된 무언가의 결과값의 자료형은....? boolean
-> True/False가 나오는 '연산자'
A in B 라고했을때 A라는 요소가 B라는 반복가능 객체 내에 존재하는지....
'''
print(5 in nums) # 결과값: True




