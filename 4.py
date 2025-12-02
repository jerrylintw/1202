"""學生成績管理：能新增成績並計算平均分數。

費曼式說明：
- 這個程式會讓你建立一位學生，記下他/她的分數，並計算平均分。
- 類比：想像一個筆記本，每次考試成績都記一筆，最後算這些分數的平均值。
"""


class Student:
    # 費曼式（建構子）：給學生一個名字，並準備一個空清單來放成績
    def __init__(self, name):
        self.name = name
        self.scores = []  # 成績列表

    # 新增成績到清單裡
    # 類比：考試完把分數寫在筆記本下一行
    def add_score(self, score):
        self.scores.append(score)  # 新增成績

    # 計算平均分
    # 1) 把所有成績加總後除以成績數量
    # 2) 如果沒有成績就回傳 0.00
    # 3) 結果使用 round(,2) 保留兩位小數，讓輸出漂亮一點
    def calculate_average(self):
        if self.scores:  # 若有成績
            return round(sum(self.scores) / len(self.scores), 2)  # 計算平均並保留兩位小數
        return 0.00  # 若沒有成績，返回 0.00

# 主流程：讀入學生名字與操作
# 費曼：第一行輸入學生名字，第二行輸入操作數量 N
name = input()

# 建立 Student 物件，準備記成績
student = Student(name)

# 讀取接下來會有幾個操作（例如新增成績或查平均）
N = int(input())

# 處理每一個操作
for _ in range(N):
    command = input().split()
    
    if command[0] == "add":
        # add 指令會跟一個分數，把它加到學生名下
        score = int(command[1])  # 讀取分數
        student.add_score(score)  # 新增成績
    elif command[0] == "avg":
        # avg 指令請程式算平均並印出
        average = student.calculate_average()  # 計算平均
        print(f"{average:.2f}")  # 輸出格式化的平均分數
