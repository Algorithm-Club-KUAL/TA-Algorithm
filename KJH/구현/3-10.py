class Customer:
    def __init__(self, id, time, num_of_people):
        self.id = id
        self.time = time
        self.num_of_people = num_of_people

class Shop:
    def __init__(self):
        self.reserve_list = []
    
    def reserve(self, customer):
        self.reserve_list.append(customer)
        return True

class HairShop(Shop):  
    def __init__(self):
        super().__init__()
        
    def reserve(self, customer):  # customer : 예약을 하고 싶어하는 고객
        if customer.num_of_people != 1:
            return False
        for r in self.reserve_list:  # r => Customer의 instance, 예약을 한 고객
            if customer.time == r.time:  
                return False
        self.reserve_list.append(customer)
        return True

class Restaurant(Shop):
    def __init__(self):
        super().__init__()
        
    def reserve(self, customer):
        # 인원수가 2명 이상 8명 이하인 경우에만 예약
        if customer.num_of_people < 2 or customer.num_of_people > 8:  
            return False
        count = 0
        for r in self.reserve_list:
            if customer.time == r.time: # 예약시간이 같은 고객 수
                count += 1
        if count >= 2:
            return False
        self.reserve_list.append(customer)
        return True
    

def solution(customers, shops):
    hairshop = HairShop()
    restaurant = Restaurant()
    
    count = 0
    for customer, shop in zip(customers, shops):
        if shop == "hairshop":
            if hairshop.reserve(Customer(customer[0], customer[1], customer[2])):
                count += 1
        elif shop == "restaurant":
            if restaurant.reserve(Customer(customer[0], customer[1], customer[2])):
                count += 1
    
    return count