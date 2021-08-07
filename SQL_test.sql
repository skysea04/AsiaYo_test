--  由於兩題的SQL語法性質類似，這裡副上兩題的答案

-- 第一題
SELECT property.name, COUNT(*) AS room_count 
FROM room INNER JOIN property ON room.property_id = property.id GROUP BY property_id 
ORDER BY COUNT(*) DESC 
LIMIT 10;

-- 第二題
SELECT property.name, count(*) AS orders_count
FROM (room INNER JOIN orders ON orders.room_id = room.id) 
INNER JOIN property ON room.property_id = property.id
WHERE orders.created_at >= '2021-02-01' AND orders.created_at < '2021-03-01'
GROUP BY property.name
ORDER BY count(*) DESC
LIMIT 10;