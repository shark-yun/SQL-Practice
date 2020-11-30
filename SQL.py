# 引入 sqlite3 套件
import sqlite3

# 建立資料庫連線（若無資料庫則新建一個 SQLite 資料庫，本身是一個檔案），以下會建立 demo.db 資料庫
connection = sqlite3.connect('demo.db')

# 使用資料庫 cursor 指標進行 SQL 操作
cursor = connection.cursor()
# 執行 SQL 語法，新增 stocks 資料表，欄位包含 id（整數 INT）, company_name（字串 TEXT）, price（整數 INT），其中 id 為識別資料的主要欄位（PRIMARY KEY）
# NOT NULL 代表欄位不得為空值
cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS stocks (
                id INT PRIMARY KEY NOT NULL,
                company_name TEXT NOT NULL,
                price INT NOT NULL
        );
        '''
)

# commit 代表提交，才是真正的將指令在資料庫執行
connection.commit()
# 最後操作完指令記得關閉資料庫連線
connection.close()
