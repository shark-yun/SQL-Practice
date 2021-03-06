
-- 創建資料表（加上 IF NOT EXISTS 判斷是否已經有資料表，若無才創建）
CREATE TABLE IF NOT EXISTS stocks (
    id INT PRIMARY KEY NOT NULL,
    company_name TEXT NOT NULL,
    price INT NOT NULL
);

-- 新增資料
INSERT INTO stocks (id, company_name, price)
VALUES (2330, '台積電', 450),(2112, '台達電', 100);

-- 查詢資料
SELECT *
FROM stocks;

-- 更新資料
UPDATE stocks
SET company_name = '台G店'
WHERE id=2330;

-- 查詢資料
SELECT *
FROM stocks;

-- 刪除資料
DELETE FROM stocks 
WHERE id=2330;

-- 已刪除，查詢不到資料
SELECT *
FROM stocks;