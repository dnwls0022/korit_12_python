from idlelib.configdialog import changes
from importlib.resources import is_resource
from openpyxl.styles.builtins import total
from prompt_toolkit import choice
MENU ={
    '에스프레소':{
       '재료':{
           '물':50,
           '커피':10,
       } ,
        '가격':1.0,
    },
    '라떼':{
        '재료':{
            '물':200,
            '우유':150,
            '커피':24,

        },
        '가격':2.5,
    },
    '카푸치노':{
        '재료':{
            '물':250,
            '우유':100,
            '커피':24,
        },
        '가격':3.0,
    },
}
resources ={
    '물':300,
    '우유':200,
    '커피':100,
}
#주석뺴고 오히려 코드만보면이해될거같아
profit = 0
#resources['물'] -= MENU ['에스프레소']['재료']['물']*2
#resources['커피'] -= MENU ['에스프레소']['재료']['커피']*2
# 에스프레소의 재료인 물, 커피를 가지고 먼저 에스프레소를 2잔 만들고  만드는 동안의 소모한 물 커피를 resource에서 차감한다.
# 차감한것을 보여준다.print(resources)
# 남은 물,우유,커피의 잔량을 보여줌(report:보고서)
def report():
    print(f'물 :{resources['물']}ml')
    print(f'우유:{resources['우유']}ml')
    print(f'커피:{resources['커피']}g')
    print(f'돈 : ${profit}')
# is_resource_enough재료가 충분한지 매개변수(주문받은재료)를 확인하고
def is_resource_enough(order_ingredients):
    #주문받은 재료 주머니에서 '물', '커피', '우유' 등을 하나씩 꺼내서 확인합니다.
    # for 변수 in 딕셔너리:
    for item in order_ingredients:
        #주문서에 적힌 양이 자판기창고의 양보다 많다면
        if order_ingredients[item] > resources[item]:
            # 3. 손님에게 어떤 재료가 부족한지 알려주고 (f-string으로 이름 쏙!)
            print(f'죄송합니다.{item}이 부족합니다.😂')
            #음료못만든다고 알려주기 *위에서 in은 나중에 return t/f값을 가진다.
            return False
    # 5. for문을 다 돌 동안 부족한 게 없었다면? "준비 완료!"라는 뜻으로 True(참)를 반환해요.
    return True
def process_coins():
    """동전들을 입력받아 총 금액을 계산해주는 '저금통' 함수"""
    print("동전을 넣어주세요.")  # 손님에게 안내 멘트!
    total = 0.0
    # 1. 쿼터 (0.25달러)
    total += int(input('쿼터(quarters) 개수>>> ')) * 0.25
    # 2. 다임 (0.10달러)
    total += int(input('다임(dimes) 개수>>> ')) * 0.1
    # 3. 니켈 (0.05달러)
    total += int(input('니켈(nickels) 개수>>> ')) * 0.05
    # 4. 페니 (0.01달러)
    total += int(input('페니(pennies) 개수>>> ')) * 0.01
    return total  # 계산된 총액을 함수 밖으로 던져줍니다!

def if_transaction_successful(money_received,drink_cost):
    #함수 밖에 있는 profit을 여기서 다시 수정하겠다고 선언
    global profit
    # 잔돈은 받은돈-커피값(2쨰자리에서 반올림)
    change = round(money_received - drink_cost, 2)
    #만약 잔돈이 0보다크면(즉, 돈을 충분히 냈다면)
    if change >= 0:
    #음료가격만큼 누적된다 profit이 쌓인다.
        profit += drink_cost
    #잔돈을 내어준다
        print(f'잔돈 ${change}반환함')
    #계산끝
        return True
    #이게아니라면 잔돈이 0이하라면 받은 금액이모자라다고 알ㄹ려준다.
    else:
        print(f'금액 불충분. $ {money_received}합니다.')
    return False

#커피제조 함수필요재료(매개변수)커피이름 주문재료
def make_coffee(drink_name, order_ingredients):
    # 1. 주문서에 적힌 재료들('물', '커피' 등)을 하나씩 확인하면서 루프를 돕니다.
    for item in order_ingredients:
       #2. 재고resources에서 주문받은 재료item을 뺀다
        resources[item] -= order_ingredients    [item]
    #음료나옴
    print(f'{drink_name}가 나옴')

is_on = True
while is_on:
    choice = input('어떤음료를 드시겠습니까? 에스프레소/라떼/카푸치노>>>')
    if choice =='off':
        is_on = False
        print("자판기를 종료함! 🤖")
    elif choice =='report':
          report()
    elif choice in ['에스프레소','라떼','카푸치노']:
        drink = MENU[choice]
        if is_resource_enough(drink['재료']):
            money_received = process_coins()
            if if_transaction_successful(money_received, drink['가격']):
                    make_coffee(choice, drink['재료'])
    else:
        print("잘못입력")
#들여쓰기 짜증나네;;;;;;;;

