"""計算平面上兩點距離的小程式。

費曼式說明：
- 我們有兩個點 (x1,y1) 與 (x2,y2)，要算它們之間的直線距離。
- 公式是：距離 = sqrt((x1-x2)^2 + (y1-y2)^2)。
 這個檔案會讀兩個點的座標並輸出距離（四捨五入到 4 位小數）。
"""

import math


class Point:
    # 費曼式解釋（物件用途）：
    # 1) 我們用 Point 類別把一個點的 x,y 座標包成一個物件，方便傳給方法計算距離。
    # 2) 類比：像把座標寫在名片上，看到名片就知道那個點的位置。
    def __init__(self, x, y):
        self.x = x  # 點的 x 座標
        self.y = y  # 點的 y 座標

    # 計算兩點間的距離
    # 費曼式：把 x 差的平方和 y 差的平方相加，最後對它們開根號。
    # 這是畢氏定理（直角三角形斜邊長公式）的應用。
    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# 讀取點 A 的座標
x1, y1 = map(int, input().split())
# 讀取點 B 的座標
x2, y2 = map(int, input().split())

# 創建 Point 類別的實例
point_A = Point(x1, y1)
point_B = Point(x2, y2)

# 計算兩點距離
distance = point_A.distance_to(point_B)

# 輸出結果，四捨五入到小數點後 4 位
# 費曼式說明：為了讓結果讀起來漂亮，我們保留 4 位小數，像老師在考卷上要求到某個小數位。
print(f"{distance:.4f}")
