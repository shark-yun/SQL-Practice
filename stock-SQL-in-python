import sqlite3

connection = sqlite3.connect('demo.db')

# 使用資料庫 cursor 指標進行 SQL 操作
cursor = connection.cursor()

cursor.execute(
   '''
   CREATE TABLE stocks (
    id INT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    closing_price INT NOT NULL
   );
    '''
)
connection.commit()
cursor.execute(
    '''
    INSERT INTO stocks (id, name, closing_price)
   VALUES (0050,'元大台灣50',90.35),
   (0051,'元大中型100',34.71),
   (0052,'富邦科技',69.35),
    (0053,'元大電子',40.50),
    (0054,'元大台商50',23.63),
    (0055,'元大MSCI金融',18.86),
    (0056,'元大高股息',28.67),
    (0057,'富邦摩台',59.20);
     '''
)

connection.commit()


rows = cursor.execute(
   '''
    SELECT *
    FROM stocks
    WHERE closing_price > 30;
    '''
)


# 將查詢資料使用 for 迴圈印出，row[0] 代表第一個欄位，依此類推
for row in rows:
        print(f'id:{row[0]}, name:{row[1]}, closing_price:{row[2]}')


# 最後操作完指令記得關閉資料庫連線
connection.close()
