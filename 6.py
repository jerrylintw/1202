"""簡易戰鬥模擬：兩個戰士互相攻擊直到一方血量歸零。

費曼式說明：
- 每個戰士有名字、血量 (hp) 和攻擊力 (atk)。
- 每一輪兩人依序攻擊對方，造成對方血量減少，血量 <= 0 表示被打敗。
"""


class Fighter:
    # 建構子：建立一個戰士並記住名字、血量與攻擊力
    def __init__(self, name, hp, atk):
        self.name = name  # 戰士名稱
        self.hp = hp      # 戰士血量
        self.atk = atk    # 戰士攻擊力

    # 攻擊另一個戰士（把自己的攻擊力從對方的 HP 減掉）
    # 費曼式解釋：想像兩人玩拳擊，攻擊就像出拳，對方會被扣血。
    def attack(self, target):
        target.hp -= self.atk  # 減少對方的血量
        print(f"{self.name} attacks {target.name} for {self.atk} damage.")

# 讀取戰士 A 的資料
name_a, hp_a, atk_a = input().split()
hp_a, atk_a = int(hp_a), int(atk_a)

# 讀取戰士 B 的資料
name_b, hp_b, atk_b = input().split()
hp_b, atk_b = int(hp_b), int(atk_b)

# 創建兩個戰士物件
fighter_a = Fighter(name_a, hp_a, atk_a)
fighter_b = Fighter(name_b, hp_b, atk_b)

# 模擬戰鬥
# 這個迴圈代表每一個回合：A 攻擊 B，若 B 沒死則 B 反擊 A，直到一方 HP <= 0
while fighter_a.hp > 0 and fighter_b.hp > 0:
    # A 攻擊 B
    fighter_a.attack(fighter_b)
    if fighter_b.hp <= 0:
        print(f"{fighter_a.name} wins!")
        break

    # B 攻擊 A
    fighter_b.attack(fighter_a)
    if fighter_a.hp <= 0:
        print(f"{fighter_b.name} wins!")
        break
