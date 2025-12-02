"""簡易購物車模擬：可以加入商品、刪除商品以及計算總金額。

費曼式說明：
- 每個商品有名稱和價格，購物車會把商品放在一起，最後算總價。
- 類比：像你逛超商，把想買的東西放進購物籃，最後結帳時把價錢加起來。
"""


class Item:
    def __init__(self, name, price):
        self.name = name  # 商品名稱
        self.price = price  # 商品價格

class ShoppingCart:
    # 費曼式：購物車就是一個清單，裡面放商品物件。
    # 你可以想像成手邊的購物籃，商品會一個一個放進去。
    def __init__(self):
        self.items = []  # 用來儲存所有商品

    # 加入商品到購物車
    def add_item(self, item):
        self.items.append(item)

    # 根據名稱移除商品（只移除第一個符合的）
    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)  # 移除第一個符合名稱的商品
                break

    # 計算總金額
    # 費曼式：把購物車裡每個商品的價格加起來，就是總價。
    # 類比：把收據上的每一筆金額加總，得到要付的錢。
    def get_total(self):
        total = sum(item.price for item in self.items)  # 計算所有商品價格的總和
        return total

# 程式主流程：建立購物車，接收指令，並根據不同指令執行動作
cart = ShoppingCart()

# 讀取接下來有幾個指令
N = int(input())

# 處理每一條指令
for _ in range(N):
    command = input().split()
    
    if command[0] == "add":
        name = command[1]
        price = int(command[2])
        item = Item(name, price)  # 創建商品物件
        cart.add_item(item)  # 加入商品到購物車
    
    elif command[0] == "remove":
        name = command[1]
        cart.remove_item(name)  # 移除商品
    
    elif command[0] == "total":
        total = cart.get_total()  # 計算總金額
        print(f"Total: {total}")
