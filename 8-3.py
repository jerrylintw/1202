"""停車場模擬：
輸入
 第一行：容量 C
 第二行：指令數 N
 接下來 N 行：park [plate] / leave [plate] / status

輸出
 park 成功 -> "Parked"，失敗 -> "Full"
 leave 成功 -> "Left"，找不到車 -> "Car not found"
 status -> "Available: x"
"""
import sys


class Car:
    # 費曼式解釋：
    # 1) 我是用最簡單的語句說明這個類別是什麼 -> Car 就是一個「車」的資料盒，裡面只有車牌號碼。
    # 2) 類比：像把一張車牌貼在一個便條上，這個便條就是 Car 的物件。
    # 3) 重點總結：Car 只是用來裝車牌的容器，程式會用它來記錄哪台車要停進停車場。
    def __init__(self, license_plate: str):
        # license_plate: 車牌號碼（例如 "ABC-123"），是 Car 這個物件最重要的資訊。
        self.license_plate = license_plate


class ParkingLot:
    # 費曼式解釋：
    # 1) 這個類別代表一個停車場，它知道總共可以停幾台車和現在有哪些車停著。
    # 2) 類比：想像一個有固定數量抽屜的櫃子 - capacity 是抽屜總數，occupied_slots 代表已被佔用的抽屜。
    # 3) 重點總結：ParkingLot 的工作是管理「有沒有空位」以及哪台車在裡面。
    def __init__(self, capacity: int):
        # capacity: 停車場的總車位數（整數）
        self.capacity = capacity
        # occupied_slots 用 set 儲存車牌，集合（set）可以快速判斷一張車牌有沒有被記錄。
        # 為什麼用 set？因為查找/移除元素很快，而且不會重複記錄同一張車牌。
        self.occupied_slots = set()

    def get_available(self) -> int:
        # 費曼式解釋：
        # 1) 這個方法算還剩下多少車位：總車位數 - 已被佔用的車位數。
        # 2) 類比：如果有 10 格抽屜，已經放了 3 個東西，還剩 7 格可以放。
        # 3) 因此我們回傳一個整數告訴程式（或人）還能停幾台車。
        return self.capacity - len(self.occupied_slots)

    def park(self, car: Car) -> bool:
        # 費曼式解釋：
        # 1) 想像你要把一台車停進停車場，我們要檢查兩件事：
        #    a) 還有沒有剩下的車位？ b) 這台車是不是已經在停車場裡了？
        # 2) 類比：像是把一個新的貼紙貼進抽屜，如果抽屜滿了或貼紙已存在，就不能再貼。
        # 3) 如果有空位且這張車牌尚未出現過，我們把車牌加入 occupied_slots，並回傳 True 表示停車成功。
        if self.get_available() > 0 and car.license_plate not in self.occupied_slots:
            self.occupied_slots.add(car.license_plate)
            return True
        # 如果沒有空位或車牌已經存在（重複停車），就回傳 False 表示停車失敗。
        return False

    def leave(self, license_plate: str) -> bool:
        # 費曼式解釋：
        # 1) 當有車要離開時，我們要檢查這張車牌是不是在停車場裡。
        # 2) 類比：像找抽屜裡的那張便條，如果有就拿掉（釋放空位），沒有就代表我們找不到那台車。
        # 3) 成功找到並移除就回傳 True，找不到就回傳 False。
        if license_plate in self.occupied_slots:
            self.occupied_slots.remove(license_plate)
            return True
        return False


def solve():
    # 費曼式解釋：
    # 1) 這裡我們把整份輸入讀進來，分成一個一個的字串（tokens），方便依序處理。
    # 2) 類比：就像把老師丟過來的一張考卷拆成每題，然後一題一題看。
    # 3) 我們後面會從這個字串清單逐項抓出容量、指令個數和每一條指令。
    data = sys.stdin.read().strip().split()
    if not data:
        return

    # data layout: C N [commands...]
    # 讀出第一個數字 C：停車場的容量
    try:
        C = int(data[0])
    except Exception:
        # 如果這裡發生錯誤（不是數字），就直接結束程式
        return

    # 讀出第二個數字 N：接下來會有幾條指令
    try:
        N = int(data[1])
    except Exception:
        # 如果 N 錯誤，就假設沒有指令
        N = 0

    # 建立一個停車場物件，我們會用它來管理停車的邏輯
    parking = ParkingLot(C)

    # idx 用來追蹤我們目前在 data 清單的哪個位置
    idx = 2
    # out_lines 收集所有要輸出的每一行文字，最後再一起印出
    out_lines = []
    for _ in range(N):
        # 如果輸入比預期短，就安全地跳出
        if idx >= len(data):
            break
        # 取出本次指令的第一個詞，例如 park / leave / status
        cmd = data[idx]
        idx += 1

        if cmd == "park":
            # park 指令會接上一個車牌，像 "park ABC-123"
            # 費曼式解釋：我們先拿到車牌，建立一個 Car 物件，然後呼叫 parking.park()
            # 如果成功就記錄 "Parked"，失敗（例如停車場滿）就記錄 "Full"。
            if idx < len(data):
                plate = data[idx]
                idx += 1
                car = Car(plate)
                if parking.park(car):
                    out_lines.append("Parked")
                else:
                    out_lines.append("Full")

        elif cmd == "leave":
            # leave 指令也會接上一個車牌
            # 費曼式解釋：這是車子離開的動作，我們要從停車場中移除這張車牌。
            # 如果移除成功就回報 "Left"，找不到該車牌則回報 "Car not found"。
            if idx < len(data):
                plate = data[idx]
                idx += 1
                if parking.leave(plate):
                    out_lines.append("Left")
                else:
                    out_lines.append("Car not found")

        elif cmd == "status":
            # status 指令不需額外參數，只要回傳還剩多少車位
            # 費曼式解釋：status 就像問櫃子還剩多少抽屜可以放東西，我們用 get_available() 計算後印出。
            out_lines.append(f"Available: {parking.get_available()}")

    # 最後把所有要輸出的文字用換行接起來輸出
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
