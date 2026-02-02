import random

from IPython.core.display_functions import display

word_list = ['apple', 'banana', 'orange', 'grape']
chosen_word = random.choice(word_list)

# 1. 비어있는  리스트 display만들기
display = []

# list 에 element를 추가
#display.append('김')
#display.append('영')
#print(display)

#display[1] = 1   # 인덱스가 생겼기 때문에가능
#print(display)
# display[4] = 4   # 애는 인덱스가 아직없어서 불가
# print(display)

#2. chosen_word 의 각 문자 개수마다 '_'추가 하기 예로 chosen_word= 'apple'이라면 display = ['_','_'''''']
for _ in range(len(chosen_word)):
    display.append('_')
print(display)
#3. chosen-word의 각 문자들을 반복시켰을때 그 위치가 guess와 일치한다면
# 해당 위치의 display에 문자를 공개한다 예로 chosen-word가
# apple이고 guess == 'p' 라면 display = ['_''p''p''_''_']로 바뀌어야한다.
guess = input('알파벳 하나를 추측해보세요>>> ').lower()
# 특정 index에 있는 '_ '
# chosen_word의 i가 guess와 일치한다면 display [i]  guess로 재대입.

##1.언제 그냥 for문쓰고 vs2.언제 향상된 for문쓰는지...
# 일반 for문 (for i in range(len(...))):
# - 언제 써요?: "3번 칸에 있는 밑줄을 알파벳으로 바꿔!" 처럼 특정 위치를 지정해서 데이터를 수정해야 할 때 반드시 써야 합니다.
# 향상된 for문 (for letter in chosen_word):
# - 언제 써요?: 그 물건이 어디(몇 번째)에 있는지는 중요하지 않고, 내용물만 훑어볼 때 써요.

#3. for _ in range(len(chosen_word)): len앞에 1을 넣으면 콘솔이 이상하게 뜨는데왜그런지

#4. 콘솔에 ['a', '_', '_', '_', '_']뜨는원리
#5. 왜 향상된 for문으러 작성했는지

for i in range(len(chosen_word)):
    if guess == chosen_word[i]:      # 일치한다면 ==
           display[i] = guess        # 재대입   =
print(display)
# 대입 ---index요소를 넣어야





