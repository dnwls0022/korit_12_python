import random
numbers = [1,2,3,4,5,]
chosen_number = random.choice(numbers)
#랜덤이라는 객체에 초이스라이는 매서드가있고 내부에 리스트 자료형넣으면 하나를뽑아서 변수에저장한다
print(chosen_number)

word_list = ['apple','banana','mango']
# todo -1 : world_list 에서 하나의 단어를 임의로 선택하도록 random모듈을 사용하고 해당단어를 chosen_word변수에 담기 v
# todo -2 : 사용자에게 알파벳 하나를 추측해서 입력하라고 요청하고
# 이를 guess변수에 담기 대문자로 시작하는경우를 방지하기위해 .lower()사용
# todo -3 : guess에서 입력한 문자하나가 chosen_word의 str문자열 중에
# 하나의 문자와 일치하는지 확인할수 있도록 반복 조건문을 작성하고
# 맞으면 정당 틀리면오답이라고 출력
'''
예를 들어 단어가 apple 이고 p라고한다면 
오답
정답
정답
오답.
'''
#random 모듈을 가져옴
import random

word_list = ['apple', 'banana', 'mango','watermelon','grape']
chosen_word = random.choice(word_list)

# TODO-2: 사용자에게 글자 하나를 입력받기 (int는 빼주세요!)
guess = input('알파벳 하나를 추측해보세요>>> ').lower()

# TODO-3: 기차 칸(단어의 글자들)을 하나씩 열어보기
# 비유: chosen_word가 'apple'이면 letter는 차례대로 'a', 'p', 'p', 'l', 'e'가 됩니다.
for letter in chosen_word:
    if letter == guess:
        print('정답')
    else:
        print('오답')


