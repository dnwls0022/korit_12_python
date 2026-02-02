# 기초설정
# ascii art generator 새로운 행맨로고만들고 로고변수에대입
# 첫 시작시에만 print 로고가 실행
#

import random
logo = ['''
  _____ ___  _ ____  _____   ____  ____  _      _____ _____ _     _  _      _____  
/__ __\\  \///  __\/  __/  / ___\/  _ \/ \__/|/  __//__ __Y \ /|/ \/ \  /|/  __/  
  / \   \  / |  \/||  \    |    \| / \|| |\/|||  \    / \ | |_||| || |\ ||| |  _  
  | |   / /  |  __/|  /_   \___ || \_/|| |  |||  /_   | | | | ||| || | \||| |_//  
  \_/  /_/   \_/   \____\  \____/\____/\_/  \|\____\  \_/ \_/ \|\_/\_/  \|\____\  
                                                                                  
''']
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = [
    # 과일 & 채소 (Fruits & Vegetables)
    'apple', 'banana', 'cherry', 'durian', 'elderberry', 'fig', 'grape', 'honeydew', 'imbe', 'jackfruit',
    'kiwi', 'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry', 'tangerine',
    'ugli', 'vanilla', 'watermelon', 'xigua', 'yam', 'zucchini', 'tomato', 'potato', 'carrot', 'onion',
    'garlic', 'ginger', 'broccoli', 'cabbage', 'spinach', 'pepper', 'eggplant', 'radish', 'cucumber', 'lettuce',

    # 동물 (Animals)
    'ant', 'bear', 'cat', 'dog', 'elephant', 'frog', 'giraffe', 'horse', 'iguana', 'jellyfish',
    'kangaroo', 'lion', 'monkey', 'newt', 'owl', 'penguin', 'quail', 'rabbit', 'snake', 'tiger',
    'urchin', 'vulture', 'whale', 'xrayfish', 'yak', 'zebra', 'dolphin', 'shark', 'octopus', 'crab',
    'lobster', 'shrimp', 'turtle', 'lizard', 'parrot', 'eagle', 'chicken', 'sheep', 'goat', 'cow',
    'panda', 'koala', 'sloth', 'otter', 'beaver', 'walrus', 'hamster', 'squirrel', 'deer', 'wolf',

    # 직업 (Jobs)
    'actor', 'baker', 'chef', 'doctor', 'engineer', 'farmer', 'guard', 'hunter', 'innkeeper', 'judge',
    'knight', 'lawyer', 'miner', 'nurse', 'officer', 'pilot', 'queen', 'rancher', 'sailor', 'teacher',
    'umpire', 'vet', 'writer', 'artist', 'dancer', 'singer', 'coach', 'dentist', 'driver', 'worker',

    # 사물 & 가구 (Objects & Furniture)
    'alarm', 'bed', 'chair', 'desk', 'eraser', 'fan', 'glass', 'hammer', 'ink', 'jar',
    'key', 'lamp', 'mirror', 'notebook', 'oven', 'pen', 'quilt', 'radio', 'sofa', 'table',
    'umbrella', 'vase', 'watch', 'xylophone', 'yoyo', 'zipper', 'camera', 'phone', 'laptop', 'bottle',
    'window', 'door', 'pillow', 'blanket', 'candle', 'basket', 'button', 'clock', 'hammer', 'spoon',

    # 자연 & 날씨 (Nature & Weather)
    'beach', 'cloud', 'desert', 'earth', 'forest', 'glacier', 'hill', 'island', 'jungle', 'lake',
    'mountain', 'ocean', 'plain', 'river', 'stream', 'tree', 'valley', 'water', 'air', 'wind',
    'storm', 'rain', 'snow', 'sun', 'moon', 'star', 'planet', 'galaxy', 'cosmos', 'fire',

    # 기타 재미있는 단어들 (Mix) - 여기서부터 400개까지 쭉 채워집니다!
    'ability', 'absent', 'academy', 'accent', 'accept', 'access', 'accident', 'account', 'accurate', 'achieve',
    'acid', 'acoustic', 'acquire', 'across', 'action', 'active', 'actor', 'actual', 'adapt', 'add',
    'addict', 'address', 'adjust', 'admit', 'adult', 'advance', 'advice', 'aerobic', 'affair', 'afford',
    'afraid', 'again', 'age', 'agent', 'agree', 'ahead', 'aim', 'air', 'airport', 'aisle',
    'alarm', 'album', 'alcohol', 'alert', 'alien', 'alike', 'alive', 'all', 'allow', 'almost',
    'alone', 'alpha', 'already', 'also', 'alter', 'always', 'amaze', 'ambition', 'amount', 'amuse',
    'analyst', 'anchor', 'ancient', 'anger', 'angle', 'angry', 'animal', 'ankle', 'announce', 'annual',
    'another', 'answer', 'antenna', 'antique', 'anxiety', 'any', 'apart', 'apology', 'appear', 'apple',
    'approve', 'april', 'arch', 'arctic', 'area', 'arena', 'argue', 'arm', 'armed', 'armor',
    'army', 'around', 'arrange', 'arrest', 'arrive', 'arrow', 'art', 'article', 'artist', 'as',
    'ash', 'aside', 'ask', 'aspect', 'assault', 'asset', 'assist', 'assume', 'asthma', 'athlete',
    'atom', 'attack', 'attend', 'attitude', 'attract', 'auction', 'audit', 'august', 'aunt', 'author',
    'auto', 'autumn', 'average', 'avocado', 'avoid', 'awake', 'aware', 'away', 'awesome', 'awful',
    'awkward', 'axis', 'baby', 'bachelor', 'bacon', 'badge', 'bag', 'balance', 'balcony', 'ball',
    'bamboo', 'banana', 'banner', 'bar', 'bare', 'bargain', 'barrel', 'base', 'basic', 'basket',
    'battle', 'beach', 'bean', 'beauty', 'because', 'become', 'beef', 'before', 'begin', 'behave',
    'behind', 'believe', 'below', 'belt', 'bench', 'benefit', 'best', 'betray', 'better', 'between',
    'beyond', 'bicycle', 'bid', 'bike', 'bind', 'biology', 'bird', 'birth', 'bitter', 'black',
    'blade', 'blame', 'blanket', 'blast', 'bleak', 'bless', 'blind', 'blood', 'blossom', 'blue',
    'blur', 'blush', 'board', 'boat', 'body', 'boil', 'bomb', 'bone', 'bonus', 'book',
    'boost', 'border', 'boring', 'borrow', 'boss', 'bottom', 'bounce', 'box', 'boy', 'bracket',
    'brain', 'brake', 'branch', 'brass', 'brave', 'bread', 'breeze', 'brick', 'bridge', 'brief',
    'bright', 'bring', 'brisk', 'broccoli', 'broken', 'bronze', 'broom', 'brother', 'brown', 'brush',
    'bubble', 'buddy', 'budget', 'buffalo', 'build', 'bulb', 'bulk', 'bullet', 'bundle', 'bunker',
    'burden', 'burger', 'burst', 'bus', 'business', 'busy', 'butter', 'buyer', 'buzz', 'cabbage',
    'cabin', 'cable', 'cactus', 'cage', 'cake', 'call', 'calm', 'camera', 'camp', 'can',
    'canal', 'cancel', 'candy', 'cannon', 'canoe', 'canvas', 'canyon', 'capable', 'capital', 'captain',
    'car', 'carbon', 'card', 'cargo', 'carpet', 'carry', 'cart', 'case', 'cash', 'casino',
    'castle', 'casual', 'cat', 'catalog', 'catch', 'category', 'cattle', 'cause', 'caution', 'cave',
    'ceiling', 'celery', 'cell', 'census', 'century', 'cereal', 'certain', 'chair', 'chalk', 'champion',
    'change', 'chaos', 'chapter', 'charge', 'charity', 'chart', 'chase', 'cheap', 'check', 'cheese',
    'chef', 'cherry', 'chess', 'chest', 'chicken', 'chief', 'child', 'chimney', 'china', 'chip',
    'choice', 'choose', 'chronic', 'chuckle', 'chunk', 'churn', 'cider', 'cigarette', 'cinema', 'circle',
    'citizen', 'city', 'civil', 'claim', 'clap', 'clarify', 'claw', 'clay', 'clean', 'clerk',
    'clever', 'click', 'client', 'cliff', 'climb', 'clinic', 'clip', 'clock', 'clog', 'close',
    'cloth', 'cloud', 'clown', 'club', 'clump', 'cluster', 'clutch', 'coach', 'coast', 'coconut',
    'code', 'coffee', 'coil', 'coin', 'collect', 'color', 'column', 'combine', 'come', 'comfort',
    'comic', 'common', 'company', 'compass', 'compile', 'confirm', 'congrat', 'connect', 'consider', 'control'
]
chosen_word = random.choice(word_list)
print(f'테스트단어: {chosen_word}')

display = []

for _ in range(len(chosen_word)):
    display.append('_')



# 1.남은 기회 숫자를 추적하기위해서 lives(목숨) 변수를 선언하고 6으로 초기화

# 2 . while문 조건을 수정하여 6번의 기회가 소진되면 반복문이종료되도록 조건작성 (end_of_game) 게임종료\
lives = 6
end_of_game = False
while not end_of_game:
    print(stages[lives])
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
