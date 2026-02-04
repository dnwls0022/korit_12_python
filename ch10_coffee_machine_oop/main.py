from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#기본생성자를 통한 객체생성
menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

# menu.menu 를 활용하여 espresso라는 str을 추출하려면..?
#print(menu.menu[1].ingredients['coffee']) # 속성메서드
#객체리스트 메뉴아이템의 리스트
while is_on:
    choice = input(f'어떤음료를 드시겠습니까? {menu.get_items()}>>> ')

    #off일때 동일 report일때 메서드 호출로 현재 재료와 수익조회
    if choice == 'off':
        print('자판기가 종료되었습니다.')
        is_on = False
    elif choice == 'report':
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
    # 커피메이커의 is_resource_sufficient만들기
        if drink is not None:
            if coffe_maker.is_resource_sufficient(drink):
                # 돈계산하기
                if money_machine.make_payment(drink.cost):
                    #최종커피제조
                    coffe_maker.make_coffee(drink)


    #아까 라떼 에스프레소 카푸치노 떳던이유
    #if를 while문안으로 넣어라
    # off쓰면 f'어떤음료를 드시겠습니까? {menu.get_items()}>>> '계속 뜨는데 뜨는이유 안뜨게한방법이나,....원리..