import random
from hangman_arts import *
# * 전체데이터를가지고옴
from hangman_word_list import word_list
# from hangman_word_list 파일내에서 실행부분만 가지고오면된다.
print(logo)

chosen_word = random.choice(word_list)
print(f'테스트단어: {chosen_word}')
print(logo)

display = []

for _ in range(len(chosen_word)):
    display.append('_')



# 1.남은 기회 숫자를 추적하기위해서 lives(목숨) 변수를 선언하고 6으로 초기화

# 2 . while문 조건을 수정하여 6번의 기회가 소진되면 반복문이종료되도록 조건작성 (end_of_game) 게임종료\
lives = 6
end_of_game = False
while not end_of_game:
    print(stages[lives])
    # hangman_arts.stages html의 자식 태그부모태그
    guess = input('알파벳 하나를 추측해보세요>>> ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

      #  else:
      #      lives -= 1
      #   print(stages[lives])
      #      print(f'기회가{lives}번 나왔습니다.')
      #      if lives == 0:
      #          end_of_game = True
      #  문자하나당일치여부를 화거인하기 때문에 예상했던것과 다르게 맞추더라도 나머지문제에대해 live -=1이; 누적적으로 적용된다ㅓ. 그래ㅔ서 반복
      #   문 바깥에 작성해야한다
    if guess not in chosen_word:
        lives -= 1
        # print(stages[lives])  # 틀렸을 때만 그림이 나온다는 점이 문제
        print(f'기회가{lives}번 남았습니다.')
        if lives == 0:
            print(f'모든 기회를 잃었습니다.')
            end_of_game = True
            print(stages[lives])
            print(f'게임종료{end_of_game}')
        # 다 맞췄을 때도 end_of_game = True가 되어야 하기 때문에 별개의 조건문
    if '_' not in display:  # 다 맞췄다는 것을 의미하겠네요
        print(f'정답입니다 !! 🍎')
        end_of_game = True

    print(' '.join(display))

#lives == 0 일때 게임종료를 표시해야한다 .
# 정답을 맞혔을떄 정답입니다 표시해야한다.
# 맞추거나 틀렷을경우 안내문 출력  _p p _ _ ...
