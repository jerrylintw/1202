"""矩形工具：讀入多組寬與高，輸出面積與周長。

費曼式說明（簡單版，給國中生）：
- 這個檔案會幫你算矩形的面積與周長。
- 我們把矩形想像成一張有兩邊寬（width）和高（height）的紙，
    面積是寬乘高（多少平方單位），周長是把四邊長加起來。
"""


class Rectangle:
        # 費曼式解釋（建立物件）
        # 1) 作用：把寬和高記在一起，變成一個「矩形物件」。
        # 2) 類比：像把寬和高寫在同一張便條貼上，方便之後拿出來算。
        # 3) 重點：建構子（__init__）會把寬、和高存進物件的欄位（self.width、self.height）。
        def __init__(self, width, height):
                self.width = width
                self.height = height

    # 費曼式解釋（面積）
    # 1) 面積 = 寬 × 高
    # 2) 類比：如果每格是 1 平方單位，寬有 3 格高有 2 格，就有 3×2=6 格可以填滿。
    # 3) 因此這個方法直接回傳 self.width * self.height。
    def get_area(self):
        return self.width * self.height

    # 費曼式解釋（周長）
    # 1) 周長是把四邊長相加：寬 + 高 + 寬 + 高 = 2*(寬+高)
    # 2) 類比：像你要貼紙在矩形周圍，貼紙的長度就是周長。
    # 3) 因此這個方法用 2*(width + height) 計算。
    def get_perimeter(self):
        return 2 * (self.width + self.height)

# 讀取測試資料數量（N）
# 費曼式解釋：
# 1) 第一行會告訴程式要處理幾筆資料，例如 N=2 表示接下來會有兩行寬和高。
# 2) 類比：像老師說「這張試卷有 3 題」，所以要做 3 次讀取與計算。
N = int(input())

# 處理每一筆測試資料
for _ in range(N):
    # 每一筆輸入會有兩個整數（W 和 H）代表寬與高
    # 讀進來之後我們建立 Rectangle 物件，然後呼叫它的兩個方法算出面積與周長。
    W, H = map(int, input().split())  # 讀入寬與高
    rectangle = Rectangle(W, H)       # 建立矩形物件（把 W 和 H 存起來）
    area = rectangle.get_area()       # 計算面積，回傳一個整數
    perimeter = rectangle.get_perimeter()  # 計算周長
    # 最後把結果印出，格式是 'Area: x, Perimeter: y'
    print(f"Area: {area}, Perimeter: {perimeter}")
