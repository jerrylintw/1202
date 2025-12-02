import sys

# Car 和 ParkingLot 類別保持不變 (它們是完美的，不用動它們)
class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.occupied_slots = set()

    def get_available(self):
        return self.capacity - len(self.occupied_slots)

    def park(self, car):
        if self.get_available() > 0 and car.license_plate not in self.occupied_slots:
            self.occupied_slots.add(car.license_plate)
            return True
        return False

    def leave(self, license_plate):
        if license_plate in self.occupied_slots:
            self.occupied_slots.remove(license_plate)
            return True
        return False

# Part 3: 主程式邏輯 (加入 flush=True)
def solve_final_flush():
    
    def read_line():
        """使用 sys.stdin.readline() 並處理 I/O 錯誤。"""
        try:
            line = sys.stdin.readline()
            if not line: # 判斷是否為 EOF
                return None
            return line.strip()
        except Exception:
            return None

    # 1. 讀取 C (容量)
    line_c = read_line()
    if not line_c:
        return
    
    try:
        C = int(line_c)
    except ValueError:
        return

    parking_lot = ParkingLot(C)

    # 2. 讀取 N (指令數)
    line_n = read_line()
    if not line_n:
        return

    try:
        N = int(line_n)
    except ValueError:
        N = 0

    # 3. 處理 N 個指令
    for _ in range(N):
        command_line_str = read_line()
        
        if not command_line_str:
            break
            
        command_line = command_line_str.split()

        if not command_line:
            continue
            
        command = command_line[0]

        # --- 邏輯判斷與輸出 (關鍵：加上 flush=True) ---
        
        if command == "park":
            if len(command_line) > 1:
                license_plate = command_line[1]
                car = Car(license_plate)
                
                if parking_lot.park(car):
                    print("Parked", flush=True) # 🌟 強制輸出
                else:
                    print("Full", flush=True) # 🌟 強制輸出
        
        elif command == "leave":
            if len(command_line) > 1:
                license_plate = command_line[1]
                
                if parking_lot.leave(license_plate):
                    print("Left", flush=True) # 🌟 強制輸出
                else:
                    print("Car not found", flush=True) # 🌟 強制輸出

        elif command == "status":
            available = parking_lot.get_available()
            print(f"Available: {available}", flush=True) # 🌟 強制輸出
            
# 執行主函式
if __name__ == "__main__":
    solve_final_flush()