class MenuItem:
    """각 메뉴 아이템들을 모델링합니다."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "물": water,
            "우유": milk,
            "커피": coffee,
        }


class Menu:
    """음료 메뉴를 모델링합니다."""
    def __init__(self):
        self.menu = [
            #keyword argumemt
            MenuItem(name="라떼", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="에스프레소", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="카푸치노", water=250, milk=50, coffee=24, cost=3),
            MenuItem(name="카라멜마키아토", water=200, milk=60, coffee=26, cost=4),
        ]

    def get_items(self):
        """이용 가능한 모든 메뉴 아이템의 이름을 반환합니다."""
        options = ""
        # item 은
        for item in self.menu:
            options += f" {item.name} /"
        #매개변수는없지만 리턴은있다 call3
        return options
    #call3 유형 매개변수잇고 리턴타입 x
    def find_drink(self, order_name):
        """특정 음료를 이름으로 메뉴에서 검색합니다. 해당 아이템이 존재하면 반환하고, 그렇지 않으면 None을 반환합니다."""
        for item in self.menu:
            #스트링이 일치하면 메뉴아이템을 뽑아냇다
            if item.name == order_name:
                return item
        print("죄송합니다. 해당 아이템은 이용할 수 없습니다.")