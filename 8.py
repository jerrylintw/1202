class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate  # 車牌號碼

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity  # 停車場容量
        self.parked_cars = set()  # 用集合存儲已停放車輛的車牌號碼

    def park(self, car):
        if len(self.parked_cars) < self.capacity:  # 停車場未滿
            self.parked_cars.add(car.license_plate)  # 停放車輛
            print("Parked")
            return True
        else:  # 停車場已滿
            print("Full")
            return False

    def leave(self, license_plate):
        if license_plate in self.parked_cars:  # 車輛在停車場
            self.parked_cars.remove(license_plate)  # 讓車離開，釋放車位
            print("Left")
        else:  # 車輛不在停車場
            print("Car not found")

    def get_available(self):
        available = self.capacity - len(self.parked_cars)  # 剩餘車位
        print(f"Available: {available}")

# 讀取停車場容量
C = int(input())

# 讀取指令數量
N = int(input())

# 創建停車場實例
parking_lot = ParkingLot(C)

# 處理每條指令
for _ in range(N):
    command = input().split()
    if command[0] == "park":
        car = Car(command[1])  # 創建 Car 物件
        parking_lot.park(car)  # 停車
    elif command[0] == "leave":
        parking_lot.leave(command[1])  # 車輛離開
    elif command[0] == "status":
        parking_lot.get_available()  # 查詢剩餘車位
