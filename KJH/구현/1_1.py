from abc import * #interface 구현을 위한 라이브러리

class DeliveryStoe(metaclass=ABCMeta): #이거 걍 하세요.
    @abstractmethod #상속한 class가 구현해야될 함수 1
    def set_order_list(self, order_list): 
        pass
    @abstractmethod #상속한 class가 구현해야될 함수 2
    def get_total_price(self):
        pass

class Food: 
    def __init__(self, name, price):
        self.name = name
        self.price = price

#inheritence, 그냥 매개변수처럼 클래스를 넣어주면 됨
class PizzaStore(DeliveryStoe): 
    def __init__(self):
        main_names = ["Che","Po","Shr","pain","Meat"] #메뉴 이름
        main_price = [11100,12600,13300,21000,19500]  #메뉴 가격
        self.menu_list = []
        self.order_list = []

        for i in range(5):
            #가격&메뉴정보를 하나의 인스턴스로 묶어줌.
            self.menu_list.append(Food(main_names[i],main_price[i]))

    #주문 리스트에서 주문을 하나씩 꺼내서 저장
    #유의사항:인터페이스 클래스와 파리미터가 동일해야함.
    def set_order_list(self, order_list):
        for order in order_list:
            self.order_list.append(order)
    
    #주문에 해당하는 가격을 누적해서 total_price에 더함.
    #유의사항:인터페이스 클래스와 파리미터가 동일해야함.
    def get_total_price(self):
        total_price = 0
        for order in self.order_list:
            for menu in self.menu_list:
                if order == menu.name:
                    total_price += menu.price
                    break
        return total_price

def solution(order_list):
    delivery_store = PizzaStore()             #클래스 선언
    delivery_store.set_order_list(order_list) #주문 전달
    total = delivery_store.get_total_price()  #가격 리턴
    return total

#테스트
order_list = ["Che","Po","Shr","pain","Meat"]
print(solution(order_list))