
# 資料集推薦

這是一個基於雅卡爾指數（Jaccard Index）計算的資料集推薦系統。根據使用者的資料集歷史，找出最相似的兩位使用者並為目標使用者推薦尚未使用過的資料集。

## 功能說明

1. **計算雅卡爾指數**：衡量使用者之間的相似度，數值越高代表兩位使用者的資料集越相似。
2. **推薦系統**：根據目標使用者的歷史資料集，推薦尚未使用過的資料集，並依據推薦指數排序。

## 輸入資料格式

使用big資料檔案`data.txt` 


- `User ID`：使用者的唯一識別碼。
- `Dataset ID`：資料集的唯一識別碼。

## 執行方式

1. **安裝需求**：確保已安裝 Python 3.x 和 `pandas` 套件，若尚未安裝，使用以下命令：

    ```bash
    pip install pandas
    ```

2. **執行程式**：

    ```bash
    python question.py
    ```

3. **任務要求輸出結果**：

    ```
    1. 最相似的兩位使用者及雅卡爾指數:
       使用者: ('sylvia', 'jessica'), 雅卡爾指數: 0.38

    2. 最應推薦給 andrew 的三個資料集:
       第1名: 資料集 964, 推薦指數: 0.31
       第2名: 資料集 401, 推薦指數: 0.30
       第3名: 資料集 253, 推薦指數: 0.28
    ```



