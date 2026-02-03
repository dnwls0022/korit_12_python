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

# 자판기에들어가는 돈
profit = 0
#1. 자판기 보유량에서 에스프레소 두 잔을 추출했을 때 /  resources의 남은 물/  커피량을 딕셔너리 형태로 보여주시오.
#로직
# 아아 에스프레소에는 가격을 제외한 재료,물이 있으니까  에스프레소의 재료의 물 이게 하나의 한잔  에스프레소의 재료의 커피가 한잔이 되고 이거를
# resource에서 남은 물 우유 커피량을 보여주는거구나
# 근데 궁금한게 한줄로 못써? 그리고 딕셔너리형태로 보여주시오했는데 그럼 딕셔너리형태로출력해야하는코드가잇어야하는거아냐?
resources['물'] -= MENU ['에스프레소']['재료']['물']*2

resources['커피'] -= MENU ['에스프레소']['재료']['커피']*2
# 딕셔너리 형태로 보여주시오.출력할 때 print(resources)만 해도 파이썬은 { '물': 200, ... } 이런 식으로 딕셔너리 모양으로 출력해준다.
#for key in MENU['에스프레소']['재료']:

#resources['물'] -= MENU['카푸치노']['재료']['key'] * 2

#print(resources)

# 라뗴 한잔 뽑앗을 떄 남는 resours
#
#for stuff in MENU['라떼']['재료']:
#resources[stuff] -=MENU['라떼']['재료'][stuff]
#profit +=MENU['라떼']['가격']

#print(resources)
#print(profit)

'''
문제
# 카푸치노 가격을 콘솔에 출력
# 에스프레소의 재료를 출력
'''
#print(MENU['카푸치노']['가격'])
#print(MENU['에스프레소']['재료'])

'''
'''





# report함수 정의 영역
def report():
    print(f'물 :{resources['물']}ml')
    print(f'우유:{resources['우유']}ml')
    print(f'커피:{resources['커피']}g')
    print(f'${resources}')

def is_resource_enough(order_ingredients):  #order_ingredient= drink['재료']
    '''Docstring: 함수/클래스/메서드가 어떤 작동을 하는지 '사람들에게 ' 설명하는기술
    주문 받은 음료를 resources에서 재료차감을 하고난후 음료만들기가 가능하면 t 아니면 f

    '''
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print('죄송합니다.{item}이 부족합니다.😂')
            return False
    return True

def process_coines():
    '''
    동전을 입력 받아 전체 금액을 반환하는 함수 call3() 유형
    :return: total
    '''
    total = 0.0
    #quaters/dimes/nickels/pennies

    total += int(input('쿼퉈동전을 몇 개 넣으시겟습니까>>>'))*0.25
    total += int(input('유로동전을 몇 개 넣으시겟습니까>>>'))*0.1
    total += int(input('달러동전을 몇 개 넣으시겟습니까>>>'))*0.05
    total += int(input('엔화동전을 몇 개 넣으시겟습니까>>>'))*0.01
    return total

def if_transaction_successful(money_received,drink_cost):
    '''
    :param money_received:
    :param drink_cost:
    :return True or False:
    '''
    global profit #함수 내에서 전역변수의 값을 바꾸는 것이 바람직하지 않아서 제한걸어두었다.

    change = round(money_received - drink_cost, 2)
    if change >= 0:
        profit += drink_cost
        print(f'잔돈 ${change}반환함')
        return True
    else:
        print(f'금액 불충분. $ {money_received}합니다.')


def make_coffee(drink_name, order_ingredients): #call2()
    # 재료 감하는 부분
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f'{drink_name}가 나옴')

#들여쓰기 짜증나네;;;;;;;;

is_on = True
while is_on:
    choice = input('어떤음료를 드시겠습니까? 에스프레소/라떼/카푸치노>>>')
    # todo-1 : choice가 off라면 자판기가 종료... 라고출력하면서 반복종료
    if choice =='off':
        is_on = False
        print("자판기를 종료함! 🤖")
    # todo-2 : choice가 report라면 물:---ml 커피 :---g /돈: $몇 달러 라고 출력될수있도록작성.
    elif choice =='report':
          report()
    # todo-3 : choice가 에스프레소/라떼/카푸치노에 해당된다면 실행문으로 다음단계로직 이라고 콘솔에출력할수있도록 작성
    elif choice in ['에스프레소','라떼','카푸치노']:
        drink = MENU[choice]
        if is_resource_enough(drink['재료']):
            money_received = process_coines()
            if if_transaction_successful(money_received, drink['가격']):
                    make_coffee(choice, drink['재료'])

     # todo-4 : 오타 발생시 잘못입력했다고 콘솔에 출력하고 다음 반복으로 넘어갈수있도록작성
    else:
        print("잘못입력")
