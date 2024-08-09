# HotelBookingSystem

HotelBookingSystem  Flask  API 專案，提供訂單管理功能。簡單對訂單的創建和驗證邏輯，支持訂單的貨幣轉換以及名稱字母大小寫驗證。


## 專案結構

```
HotelBookingSystem/
├── app/
│ ├── controllers/ # 控制器，請求邏輯控制
│ ├── models/ # 模型，定義Data class
│ ├── repository/ # Database 訪問層
│ ├── schemas/ # 驗證請求格式
│ ├── services/ # 業務邏輯
│ ├── init.py # Flask初始化
├── test/ # 單元測試
├── .gitignore # 
├── app.py # 入口
├── Dockerfile # Docker配置文件
├── requirements.txt # 套件依賴
└── README.md
```
## 運行
```
git clone <project>
cd HotelBookingSystem
docker build -t hotel-booking-system .
docker run -p 5000:5000 hotel-booking-system
```
## 單元測試
```
docker exec -it "docker-id" bash  //進入docker 容器
python -m unittest discover -s test
```

題目一:
```
SELECT 
   orders.bnb_id,
   bnbs.name AS bnb_name,
   SUM(orders.amount) AS may_amount
FROM
   orders
JOIN 
   bnbs ON orders.bnb_id = bnbs.id
WHERE 
   orders.currency = 'TWD'
   AND orders.created_at >= '2023-05-01'
   AND orders.created_at < '2023-06-01'
GROUP BY
   orders.bnb_id, bnbs.name
ORDER BY 
   may_amount DESC
LIMIT 10;
```
題目二:
```
先查看執行速度慢的原因,先判斷 搜尋指令有無多餘的搜尋,如果已經是最佳
則對流程上優化,將資料庫做讀寫分離降低負擔,將常搜尋的欄位加上普通索引,提高搜尋速度
最後真的因為資料量太大而導致,會考慮分表儲存
1.資料庫讀寫分離 
2.正規化
3.硬體資源升級
4.分表(最後的選擇)
```
