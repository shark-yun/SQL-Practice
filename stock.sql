CREATE TABLE IF NOT EXISTS stocks (
    id INT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    closing_price INT NOT NULL
);

INSERT INTO stocks (id, name, closing_price)
VALUES (0050,'元大台灣50',90.35),
(0051,'元大中型100',34.71),
(0052,'富邦科技',69.35),
(0053,'元大電子',40.50),
(0054,'元大台商50',23.63),
(0055,'元大MSCI金融',18.86),
(0056,'元大高股息',28.67),
(0057,'富邦摩台',59.20);

SELECT *
FROM stocks
WHERE closing_price > 50;
