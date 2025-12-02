"""銀行帳戶模擬。

費曼式說明（簡單版）：
- 這個程式會模擬一個簡單的銀行帳戶，可以存款、提款，最後輸出餘額。
- 類比：把錢放在一個罐子（帳戶），存就放進去，提就拿出來，不能多拿超過罐子裡的錢。
"""


class Account:
    # 費曼式解釋（建構子）
    # 1) Account 代表一個人的銀行帳戶，它有一個帳號和餘額。
    # 2) 類比：像在銀行開了一個戶頭，帳號是戶頭編號，balance 是你罐子裡的錢。
    def __init__(self, account_number, balance):
        self.account_number = account_number  # 帳號，字串
        self.balance = balance  # 初始餘額，整數

    # 存款（把錢放進罐子）
    # 費曼式：把 amount 加進餘額中，等於你把錢放進去。
    def deposit(self, amount):
        self.balance += amount

    # 提款（拿錢出來）
    # 費曼式：如果罐子裡錢夠，從裡面扣掉 amount 並回傳 True；如果錢不夠，回傳 False，表示提款失敗。
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

    # 查詢餘額（看看罐子裡還剩多少錢）
    def check_balance(self):
        return self.balance

# 讀取帳號和初始餘額（第一行）
# 範例輸入："A123 100" -> 帳號 A123，初始餘額 100
account_number, balance = input().split()
balance = int(balance)

# 創建 Account 類別實例
account = Account(account_number, balance)

# 讀取接下來有幾條指令（N）
N = int(input())

# 處理每一條指令
for _ in range(N):
    # 每條指令格式例如：deposit 50 或 withdraw 30
    command = input().split()
    action = command[0]
    amount = int(command[1])
    
    if action == "deposit":
        # 存款，不需要輸出，只改變帳號內餘額
        account.deposit(amount)
    elif action == "withdraw":
        # 提款時會回傳成功或失敗，失敗則印出提示
        if account.withdraw(amount):
            print("Success")
        else:
            print("Insufficient funds")

# 程式結束時輸出最後剩下的錢
print(f"Final Balance: {account.check_balance()}")
