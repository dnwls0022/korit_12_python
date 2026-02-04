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
profit = 0
# 1. 남은재료보여주는함수정의
def report():
    print(f'물 :{resources['물']}ml')
    print(f'우유:{resources['우유']}ml')
    print(f'커피:{resources['커피']}g')
    print(f'돈 : ${profit}')
# 2. 주문을받고 재료가 충분한지알려주는 함수
def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'죄송합니다.{item}이 부족합니다.😂')
            return False
    return True
# 3. 동전을입력받아 금액계산하는함수
def process_coins():
    """동전들을 입력받아 총 금액을 계산해주는 '저금통' 함수"""
    print("동전을 넣어주세요.")
    total = 0.0
    total += int(input('쿼터(quarters) 개수>>> ')) * 0.25
    total += int(input('다임(dimes) 개수>>> ')) * 0.1
    total += int(input('니켈(nickels) 개수>>> ')) * 0.05
    total += int(input('페니(pennies) 개수>>> ')) * 0.01
    return total
# 4. 연산이 성공적으로 되었는지 보여주는함수 매개변수로 돈을받고 음료재료를받음
def if_transaction_successful(money_received,drink_cost):
    global profit
    change = round(money_received - drink_cost, 2)
    if change >= 0:
        profit += drink_cost
        print(f'잔돈 ${change}반환함')
        return True
    else:
        print(f'금액 불충분. $ {money_received}합니다.')
    return False
# 5. 커피제조기 함수
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
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


