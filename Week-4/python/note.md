
```python
def change_calculator(price):
    # 1. 計算總共需要找多少錢
    total_change = 100 - price

    # 如果金額超過 100，代表錢不夠付
    if total_change < 0:
        print("付款金額不足！")
        return

    # 2. 定義硬幣面額
    denominations = [50, 10, 5, 1]

    # 用來存放結果的字典或列表
    results = {}

    # 3. 核心邏輯：使用迴圈處理每一種面額
    remaining = total_change
    for coin in denominations:
        # 計算該面額可以換幾枚 (整數除法)
        count = remaining // coin
        # 儲存結果
        results[coin] = count
        # 更新剩餘需要找的金額 (取餘數)
        remaining = remaining % coin

    # 4. 依照題目要求的格式輸出
    output = f"50 元 {results[50]} 枚，10 元 {results[10]} 枚，5 元 {results[5]} 枚，1 元 {results[1]} 枚"
    print(output)

# --- 測試範例 ---
print("測試 1 (price=21):")
change_calculator(21)

print("\n測試 2 (price=65):")
change_calculator(65)

print("\n測試 3 (price=100):")
change_calculator(100)
```

```

---

### 程式邏輯詳細解析

這段程式的運作步驟如下：

1.  **計算找零總額**：
    *   `total_change = 100 - price`。例如輸入 21，找零就是 79 元。

2.  **使用「整數除法 (`//`)」與「取餘數 (`%`)」**：
    這是解決找零問題最有效率的方法。
    *   **以 79 元為例：**
        *   **處理 50 元**：
            *   `79 // 50 = 1` (得到 1 枚 50 元)。
            *   `79 % 50 = 29` (剩下的錢是 29 元)。
        *   **處理 10 元**：
            *   `29 // 10 = 2` (得到 2 枚 10 元)。
            *   `29 % 10 = 9` (剩下的錢是 9 元)。
        *   **處理 5 元**：
            *   `9 // 5 = 1` (得到 1 枚 5 元)。
            *   `9 % 5 = 4` (剩下的錢是 4 元)。
        *   **處理 1 元**：
            *   `4 // 1 = 4` (得到 4 枚 1 元)。
            *   `4 % 1 = 0` (找完了)。

3.  **輸出格式化**：
    使用 Python 的 `f-string` 功能，可以輕鬆地將計算出的數值填入字串中，達到題目要求的格式：`50 元 X 枚，10 元 X 枚
...`。

### 執行結果範例

當你執行上述程式後，畫面會顯示：

```text
測試 1 (price=21):
50 元 1 枚，10 元 2 枚，5 元 1 枚，1 元 4 枚

測試 2 (price=65):
50 元 0 枚，10 元 3 枚，5 元 1 枚，1 元 0 枚

測試 3 (price=100):
50 元 0 枚，10 元 0 枚，5 元 0 枚，1 元 0 枚
```