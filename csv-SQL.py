# 引入模組套件
import sqlite3
import pandas as pd

# 建立 table 資料表 SQL 指令
create_table_sql = """
        CREATE TABLE IF NOT EXISTS
        stocks (
            id TEXT PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            closing_price INT NOT NULL
        );
        """

# 使用 sqlite3 套件建立資料表，建立資料庫連線
with sqlite3.connect('stocks.db') as conn:
    # 取得操作資料庫指標
    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    # 若非查詢語法需要提交到資料庫才算完成
    conn.commit()

# 將 csv 檔案使用 Pandas 讀入成為 Dataframe
df = pd.read_csv('stocks.csv', encoding='utf-8')

# 取出證券代號，證券名稱，收盤價。loc[index 範圍（: 代表所有）, [欄位]]
stock_data = df.loc[:, ['證券代號', '證券名稱', '收盤價']]

# 使用 iterrows 一一取出 Dataframe 每一列資料。由於取出的 index 沒使用也可以寫成 _ 佔位符號
for index, row in stock_data.iterrows():
    insert_data_sql = f"""
            INSERT INTO stocks (id, name, closing_price)
            VALUES ('00{row['證券代號']}', '{row['證券名稱']}', {row['收盤價']});
            """
    # 新增插入資料
    with sqlite3.connect('stocks.db') as conn:
        cursor = conn.cursor()
        cursor.execute(insert_data_sql)
        # 若非查詢語法需要提交到資料庫才算完成
        conn.commit()

# 建立查詢 SQL 語法
query_data_sql = """
        SELECT * FROM stocks WHERE closing_price > 30 
        """

# 查詢資料
with sqlite3.connect('stocks.db') as conn:
    cursor = conn.cursor()
    rows = cursor.execute(query_data_sql)

# 使用 for 迴圈取出結果
for row in rows:
    print(f'id: {row[0]}, name: {row[1]}, closing_price: {row[2]}')
