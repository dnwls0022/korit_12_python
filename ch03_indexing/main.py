str_example = 'Hello World'
print(str_example[0])
print(str_example[1])
print(str_example[2])
print(str_example[3])
print(str_example[4])
print(str_example[5])
print(str_example[6])

print(len(str_example))

'''
len() : 반복 가능 객체의 전체 인덱스 값을 return하는 함수

'''

# 향상된 for문으로 'Hello World'한줄 출력
#일반 for문으로 'Hello World'한줄 출력
# for i in range(10):
#     print(i+1)향상된 for문의 파이썬형식 !!!!!!!!
for letter in str_example:
    print(letter)

for letter in str_example:
    print(letter, end="")

'''
마이너스 인덱스 : 문자열의 인덱스를 활용하여 한 문자 이상으로 구성된 단어나 문장을 추출할 때 사용 추출하고자하는 단어나 문장의 시작 인덱스와 종료 
인덱스를 통해 그 사이 문자들을 추출하는것이가능

형식:
변수명[시작인덱스: 종료인덱스:증감값]
시작인덱스: 생략하면 처음부터 추출
종료인덱스: 생략하면 끝까지추출
증감값 : 생략하면 1씩 증가(인덱스넘버가 0부터1 씩 증가한다)
'''
print()
print(str_example[:-3:])

print(str_example[:-1:])
print(str_example[:-2:])
print(str_example[:-3:])
print(str_example[:-4:])
print(str_example[:-5:])
print(str_example[:-6:])

'''
range(시작값,종료값,증감값)
변수명[시작인덱스:종료인덱스:증감값]이랑 똑같음 . 하나는 : 이거이고  다른하나는 ,?\

네자리숫자를 입력받아 그 자리의 맨 마지막 숫자 출력
'''
number = int(input("네 자리 숫자를 입력하세요>>>"))
print(type(number))
print(f'맨 마지막숫자는 {number-1}입니다.')

if int(number[-1])%2==0:
    print(f'맨 마지막 숫자는 {number[-1]}이며 짝수이다.')
else:
    print(f'맨 마지막 숫자는  {number[-1]}이며 홀수이다.')


'''
python삼항 연산자

'''
result = "짝수" if int(number[-1]) %2 == 0 else '홀수'
print(f'맨 마지막 숫자는 {number[-1]}이며 {result}입니다.')

