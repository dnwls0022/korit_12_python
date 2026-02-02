import random

word_list = ['apple','banana','mango']
chosen_word = random.choice(word_list)
print(f'테스트  {chosen_word}')

display = []

for i in range(len(chosen_word)):
    display.append('_')
print(display)

'''
''.join(반복가능객체) method : '.'앞에있는 문자열을 기준으로 반복가능객체의 element들을 합쳐서 str로 만들어주는 메서드
'''

#temp = ['s','q','k','f']
#test = ''.join(temp)

#print(test)
#test = '/'.join(temp)

#print(test)
#test = ''.join(temp)


# todo1/ 사용자가 추측을 반복할수있도록 while 반복문조건 사용
# 사용자가 chosen_word의 모든 문자열을 맞추었을떄 즉 display에 '_' 가 없을떄 반복문을 중단시킴 종료후 정답출력#
# 1.
while '_' in display:
     guess = input('알파벳 하나를 추측해보세요>>> ').lower()
     for i in range(len(chosen_word)):
         if chosen_word[i] == guess:
             display[i] = guess
     print(display)
print('정답입니다.')

# 2.
while ''.join(display) != chosen_word:
    guess = input('알파벳 하나를 추측해보세요>>> ').lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess
    print(display)
print('정답입니다.')

# todo2 정답을 보여줄때 apple이라면 a p p l e로 출력가능하도록 .join(반복가능객체) method 활용
