'''
대표 collection
1. list 리스트  추가/수정/삭제가 언제나 가능/ 순서잇음
2. tuple 튜플  추가/수정/삭제가 언제나 불가능/ 순서잇음
3. set 세트    중복값의 저장이불가능/ 순서없음
4. dict 딕셔너리   키+값으로 관리
'''



list_example = [30,40,'김이', [100, '김삼']]
#대괄호냐
print(list_example)
tuple_example = (10,20,30,'김사')
#소괄호냐
print(tuple_example)
set_example = {100,200,300, '김오'}
#중괄호냐
print(set_example)
dict_example = {'이름': '김일', '나이':20, '학교':'코리아아이티'}
print(dict_example)

'''
1. list : 여러값을 저장할때 가장 많이 사용된다. 자료형이 서로 다르더라도 하나의 리스트에 저장가능하다. java 기준하나의 배열에 동일한 자료형만
들어가는 것과 달리 강점을가짐
'''
# list의 선언 및 초기화
# li1 = [1,2,3, '김사']

'''
1) list의 index / slice
    list는 str과 동일한 방식의 index /slicing을 지원
     1) 인덱스 / 마이너스 인덱스
'''
# print(li1)
# print(li1[1])
# print(li1[2])
# print(li1[3])
# print(li1[-1])
# print(li1[-2])
# print(li1[-3])
# print(li1[-4])
...

'''
2) slicing 
    str의 slicing과 같이 '시작인덱스:종료인덱스:증감값'
'''

li2 = [100, 3.14, 'hello']
li3 = list([4,5,6,7,4,5,9]) #[4,5,6,7,4,5,9]튜플인데 list로 형변환해주었다.
print(li3)
# 리스트라고하는함수내에 특정값을 집어넣음

print(li3 [0:4:2]) # 시작인덱스부터 4번지 앞까지 2씩증가 - 4 6 출력

'''
3) list 의 element추가와 삭제
    list 에 새로운 요소를 추가할때는 .append()를 써서 사용한다 그리고 .insert도 존재
'''

scores = [30, 40 ,50]
print(scores)
scores.append(100)
print(scores)
scores.insert(1,200)
print(scores)       #결과 [30, 200, 40, 50, 100]

'''
삭제관련 
.pop의 경우 NoArgs라면 맨마지막 element가 삭제된다. 
.pop(인덱스넘버) 로 작성하면 해당 인덱스의 마지막 element를 삭제한다
'''

print(scores.pop())  # 결과값 : 100 마지막인덱스의 element를 삭제한다

print(scores)

print(scores.pop(0))
print(scores)
'''
***+ 삭제메서드 : .remove(값) 
'''
print(scores.remove(50))
# scores.remove(300)
#scores.pop(10)
print(scores)

'''
li4 리스트를 선언하고, 1부터 10까지 집어 넣어 보세요.
print(li4) 결과값은 [1,2,3,4,5,6,7,8,9,10]

각 list 내의 element들을 뽑아내서 * 2씩 시키겠습니다.
일반 for문 형식으로 한 번
enhanced for문 형식으로 한 번 해서 첫 번째 element가 4가 되어야겠습니다.
'''
li4 = []
for i in range(1,11):
    li4.append(i)
    print(li4)

for i in range(len(li4)):
    li4[i] *= 2
    print(li4)

print('[', end=' ')
for num in li4:
    num *= 2
    if num == 40:
        print(num, end=' ')
    else:
        print(num, end=', ')
print(']', end=' ')

# 귀찮다는 것을 알았습니다. 사실상 list 내에서의 element들에 대해 연산을 일괄적으로 적용하는 method가 따로 있습니다. 그리고 우리는 그것을 JS에서 해보기도 했습니다.
print()
modified_li4 = list(map(lambda num: num*2, li4))
# 이상의 경우가 극단적으로 list의 내부 각각의 element들에 동일한 함수를 적용한 결과를 적용하는 map() 함수입니다. 그런데 저희는 JS에서 배열의 method로 사용했었습니다. 이상의 코드가 좀 문제가 있다면 map()함수의 결과값이 map 객체에 해당하기 때문에 list() 함수를 통한 형변환을 해줘야한다는 점입니다.
print(modified_li4)
'''
2. tuple : 저장된 값을 변경할수없는 list ... 순서는있기 떄문에 index넘버의 사용과 slicing가능
'''
# 튜플생성법 1.2.3
tu1 = (1,2,3)
tu2 = tuple([4,5,6])
tu3 = 7,8,9


print(type(tu3))
a, b, c = 7, 8, 9 #복수의 변수 선언 및 초기화 방법  => 변수 개수와 데이터 개수가 같으면 알아서 순서대로대입.

# tu4 = 0

tu5 = 'hello' , 'good morning.', 'my name is' , 'kim -il', 'i am', '20', 'year old'

for word in tu5:
    print(word.title(),end='')
    # 결과값:

print()
print(tu5)
'''
collection개념과 내부 element의 자료형이 서로다르다. tuple 자체는 추가/수정/삭제가 불가했다. 근데 내부 element자체는 str이니 데이터의 가공
가능
'''

'''
3. set
집합개념 
'''

set1 = {1,2,3}
set2 = set({4,5,6})

li = []
tu = ()
se = {}
se1 = set({})
print(type(li))
print(type(tu))
print(type(se))
'''
set관련 메서드 
1. .add() - set에 새로운 element추가
2. .remove()
3. .discard()

'''

se3 = {10,20,30}
se3.add(50)
print(se3)
se3.remove(30)
print(se3)

#remove() vs discard()
#se3.remove(70) #오류
#print(se3)
se3.discard(70) #오류 x
print(se3)

'''
.remove()의 경우  argument로 set내에 있는 값을 정확하게 입력하지않으면 keyError .예외가발생합니다. 반면에 discard()의 경우에는 set내에
없는 값을 입력했을 경우해당 값이 애초 존재하지않기떄문에 그대로 값이나온다.
'''

# 인덱스 넘버는 없지만 향상된 for문으로 내부 element출력가능
for num in se3:
    print(num) #순서는 다를수잇음

'''
4. dict(ionary) - 자바의 맵 자바스크립트이 오브젝트, json과비슷
'''
dict1 ={
    '이름': '김일',
    '나이':20,
    '주소': ['서울특별시', '마포구', '목동'],
}

'''
179번까지 key-value-pair가 있는데 나중에 학교라는 key를 추가하라고할때 179번라인에 콤마후 엔터치고 '학교': '코코코코' 라는식으로 번거로우니
나중에 확장성을 위해 미리 콤마한다.


'''
for key in dict1:
    print(key)

for key in dict1:
    print(dict1[key])

print(dict1.keys())
print(type(dict1.keys()))
print(list(dict1.keys()))

print(dict1.values())
print(type(dict1.values()))

# key 혹은 value 들만 뽑아서 list를 만들고싶다면 list()형변환 함수를 사용

'''
collection수업할때 중요한것은 list를 배웠을때

'''
dict1['직업'] = '웹 퍼블리셔'
print(dict1)
dict1['직업'] = '웹 개발자'
print(dict1)

print(dict1.pop('직업'))  # pop은 리턴된다 가장최근에 추가한 직업이 따로 return되어서 보여진다.  결과: 웹 개발자

'''
응용 예제

list [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]의 3번째 요소로부터 7번째 요소만 추출한 결과, 그리고 그
list에서 2 번째 요소를 출력하는 프로그램을 작성하시오.

실행 예
3 번째 요소로부터 7 번째 요소 = [30, 40, 50, 60, 70]
3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = 40

'''
list1 =  [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(f'3 번째 요소로부터 7 번째 요소 = {list1 [2:7]}')
# print(f'3 번째 요소로부터 7 번째 요소 = {list1 [2:7][1]}')
print(f'3 번째 요소로부터 7 번째 요소 = {list1.pop(3)}')



'''
실행 예
3 번째 요소로부터 7 번째 요소 = [30, 40, 50, 60, 70]
3 번째 요소로부터 7 번째 요소 중 2 번째 요소 = 40

1.사용자로부터 1에서 12사이의 월을 입력 받아, 해당 월이 며칠까지 있는지 출력하는 프로그램을 작성하시오.
(윤년은 고려 x)

실행 예
1 ~ 12 사이의 월을 입력하세요 >>> 2
2월은 28일까지입니다.
2. # 1 : dictionary를 이용하는 방법
2. # 2 : list를 이용하는데, [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]을 이용하는 방법
2. # 3 : list를 이용하는데, [28, 30, 31]을 이용하는 방법
'''
# 사용자에게 월 입력받기
month = input('1-12사이의 월을 입력하세요 >>>')


#2-1 dict선언
day_dict = {

    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31,
}
#사용자에게 입력받은 값 출력
print(f'{month}월은 {day_dict[month]}일이다')



# 2-2 day -dict를 list로 선언
day_dict = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month는 정수값이니까 int로 형변환해줘야한다.
month_int = int(month)
# 1. print(f'{month}월은 {day_dict[month_int-1]}일까지입니다.') -1하는이유
# 0번째가 1월 31일 1번쨰가 2월 28일 2번쨰가 3월 31일이라서 .... 2월을 입력하면 28일이 나오도록 우리는 2월이 28일이라고 알고있지만 컴퓨터
# 는 우리가 입력한대로 2번째에 3월 31일이 되어있으니 -1 해서 자동으로 한칸뒤값이 나오도록... 이구나
print(f'{month}월은 {day_dict[month_int-1]}일까지입니다.')






#2-3  list를 이용하는데, [28, 30, 31]을 이용하는 방법
day_list2 = [28,30,31]
# 2. 입력받은 달이 2이면 마지막날은 (last date)는  day_list2[0] 28입니다
if month_int == 2:
    last_date = day_list2[0]
#위에 if문이아니면- 2월제외 2월만 28일까지있음 !  - 나머지에서 30일인 day_list2 = [28,30,31]의 1번쨰에 30이 4,6,9,11월이니까 이 달에
# 마지막날에 day_list2[1]을 대입해준다
elif month_int == 4 or month_int == 6 or month_int == 9 or month_int == 11:
    last_date = day_list2[1]
# 이것도 아니면 나머지 마지막날이 31일인 달만 1,3,5,7,8,10,12 적용한다
elif month_int in [1,3,5,7,8,10,12]:
    last_date = day_list2[2]
# 이것도아니면 마지막 else를 적용
else:
    print("잘못입력")
    last_date = 'x'

print(f'{month}월은 {last_date}일 까지입니다.')



'''
이상의 코드 라인에서 중요한 것은 in 개념입니다.
in 뒤에는 다양한 것들이 올 수 있는데, 특히 반복가능객체(iterable)이 올 수 있다는 점입니다.
그래서 
elif month_int in [ 1, 3, 5, 7, 8, 10, 12 ]:
    last_date = last_date_list2[2]
의 해석 부분이 중요한데, in 다음에 임의의 list를 초기화하여 month_int가 임의의 list의 element값을 가지고 있는지 여부를 조건 검토했다고 해석할 수 있겠습니다.

( 1, 3, 5, 7, 8, 10, 12 ) 이렇게 초기화하더라도 전혀 문제가 없겠네요. tuple로 집어넣은 사례가 되겠습니다.
'''


'''
응용 예제
1.수학 여행을 어디로 갈 지 결정하기 위해 학생들이 희망하는 모든 수학 여행 장소를 조사하기로 했습니다.
 학생들이 원하는 장소를 입력 받아
동일한 입력을 무시하고 모든 입력을 저장하려고 합니다.
학생을 3 명으로 가정하고 실행 예와 같이 동작하는 프로그램을 작성하시오.

실행 예

희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 제주
희망하는 수학여행지를 입력하세요 >>> 민속촌

조사된 수학여행지는 {'제주', '민속촌'}입니다.
조사된 수학여행지는 ['제주', '민속촌']입니다.
'''
# 1.field_trip_set= set() ????
field_trip_set= set()
# 학생을 3 명으로 가정하고
num_of_students = 3
# 학생3명의 값이 있는동안
for _ in range(num_of_students):
    # 2. student = input("희망하는 수학여행지를 입력하세요 >>")??? 왜 여기서 받지 처음에안받고
    # 아아 첨에 물어보면 한번만 물어보고 끝나고 for문안에서 물어보면 3번 3명의학생에게 다 물어보는것이군
    student = input("희망하는 수학여행지를 입력하세요 >>")
    # 학생3명의 대답을 여행지(field_trip_set) 에 추가한다.
    field_trip_set.add(student)

print(f'조사한 수학 여행지는 {field_trip_set}입니다.') # 중괄호 { } 형태의 '집합(set)' 그대로 출력
print(f'조사한 수학 여행지는 {list(field_trip_set)}') #중복제거된것을 '리스트' 모양으로 바꿔서 출력
'''
2. 짝수만 추출하기

사용자로부터 임의의 양의 정수를 입력 받고, 그 정수만큼 숫자를 입력 받아 list에 저장하세요.
이 후 저장된 숫자 중 짝수만 새로운 list에 저장하여 출력하는 프로그램을 작성하세요.

실행 예
몇 개의 숫자를 입력할까요? >>> 5
1번째 숫자를 입력하세요 >>> 10
2번째 숫자를 입력하세요 >>> 15
3번째 숫자를 입력하세요 >>> 20
4번째 숫자를 입력하세요 >>> 25
5번째 숫자를 입력하세요 >>> 30
입력 받은 숫자는 [10, 15, 20, 25, 30]입니다.
입력 받은 숫자들 중 짝수는 [10, 20, 30]입니다.
'''
# li_original = []
# li_even = [] ????
# 모든 전체바구니 original
li_original = []
# 짝수 = even
li_even = []
# n의 변수 프롬포트
n = int(input("몇 개의 숫자를 입력할까요? >>>"))
# n개 만큼 반복한다.
for i in range(n):
    # 밑에 프롬포트를 3번반복 +1씩 증가하면서 num은 실제 값 1번쨰에 숫자 14입력하면 이 14가 num
    num = int(input(f'{i+1} 번쨰숫자를 입력하세요 >>>'))
    # li_original.append(num) 만약13이면 li.original에 넣고append
    li_original.append(num)
    # num의 입력받은 n번째의 값이 짝수이면
    if num % 2 == 0:
        # li.even짝수를 담는 그릇에 num의 값을 넣어라
        li_even.append(num)

print(f'입력 받은 숫자는 {li_original}입니다.')
print(f'입력받은 숫자들 중 짝수는 {li_even}입니다.')

'''
딕셔너리 기반의 연락처 관리

사용자로부터 3 명의 이름과 전화번호를 입력 받아 딕셔너리에 저장한 뒤, 입력한 정보를 추출하는
프로그램을 작성하시오.

실행 예
1 번째 사람의 이름의 입력하세요 >>> 김일
1 번째 사람의 연락처를 입력하세요 >>> 010-1234-5678
2 번째 사람의 이름의 입력하세요 >>> 김이
2 번째 사람의 연락처를 입력하세요 >>> 010-2345-6789
3 번째 사람의 이름의 입력하세요 >>> 김삼
3 번째 사람의 연락처를 입력하세요 >>> 010-3456-7890

입력 받은 연락처는 {'김일':'010-1234-5678', '김이':'010-2345-6789', '김삼':'010-3456-7890'}입니다.
'''
phones={}
num_of_people =3
for i in range(num_of_people):
    dict_key = input(f'{i+1}번째 사람의 이름입력')
    dict_value = input(f'{i+1}번째 사람의 연락처입력')
phones[dict_key] = dict_value
print(f'입력 받은 연락처는 {phones}입니다.')


'''
숫자를 입력한 횟수만큼 비어있는 list에 숫자를 추가하기
문제 : 비어있는 numbers1을 선언하고, 그 안에 입력 받은 횟수만큼 숫자를 추가하시오.

함수 정의 : add_numbers()....
매개 변수 : 정수 n

함수 호출
add_numbers1(last_num)          # call2() 유형
print(add_numbers2(last_num))   # call4() 유형

실행 예
숫자 몇 까지 입력하시겠습니까? >>> 10
[1,2,3,4,5,6,7,8,9,10]
[1,2,3,4,5,6,7,8,9,10]
'''
# 매개변수n을갖는 함수 정의 : add_numbers()...
def add_numbers1(n):
    numbers = []

    #for문
    for i in range(n):
        numbers.append(i)
    print(numbers)
    # call2유형
# 프롬포트
last_num = int(input('숫자 몇 까지 입력하시겠습니까? >>>'))
add_numbers1(last_num)



#call4유형
def add_numbers2(n):
    last_num2 = []
    for i in range(1, n+1):
        last_num2.append(i)
    return last_num2
print(f'{add_numbers2(last_num)} 결과값을 가집니다.')



'''
예를 들어 hello = ['안', '녕', '하', '세', '요']라는 list가 있다고 가정했을 때,
add_numbers3(10, hello)를 호출하면
[1,2,3,4,5,6,7,8,9,10,'안','녕','하','세','요']
라는 결과값을 만드는 함수를 정의한다면 어떻게 할 수 있을지 고민해보세요.
'''
def add_numbers3(n,temp_list):
    numbers = []
    for i in range(n):
        numbers.append(i+1)
    for letter in temp_list:
        numbers.append(letter)
    print(numbers)




def add_numbers4(n, temp_list):
    for i in range(n):
        temp_list.insert(i, i+1)
    print(temp_list)


add_numbers3(10, ["안","녕"])
add_numbers4(20,['하','이'])



'''
짝수와 홀수의 개수 세기

list를 입력 받아 짝수와 홀수의 개수를 세는 함수를 작성하시오.

함수 정의
함수 이름 : count_even_odd
매개변수 : list인 numbers(요소는 모두 정수일 것)

함수 호출
count_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

실행 예
짝수의 개수 : 5개
홀수의 개수 : 5개
'''
def count_even_odd1(numbers):
    even_num = 0
    odd_num = 0

    for number in numbers:
        if number % 2 == 0:
            even_num += 1
        else:
            odd_num += 1

    print(f'짝수의 개수 :{even_num}')
    print(f'홀수의 개수 :{odd_num}')

count_even_odd1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])