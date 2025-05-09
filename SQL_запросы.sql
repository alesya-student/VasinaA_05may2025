SELECT * FROM public.categories
ORDER BY category_id ASC

-- Уникальные регионы сбора грибов.
SELECT r.name
FROM regions r
JOIN mushrooms m ON r.region_id = m.primary_region_id;


-- Грибы категории "Трубчатые" (название, сезон сбора, съедобность).
SELECT m.name, m.season, m.edible
FROM mushrooms m
JOIN categories c ON m.category_id = c.category_id
WHERE c.name = 'Трубчатые';


-- Грибов по категориям в порядке убывания.
SELECT c.name, COUNT(m.mushroom_id) AS mushroom_count
FROM categories c
JOIN mushrooms m ON c.category_id = m.category_id
GROUP BY c.name
ORDER BY mushroom_count DESC;


-- Съедобные грибы и их описание из пяти самых крупных регионов (size).
SELECT m.name, m.description
FROM mushrooms m
JOIN regions r ON m.primary_region_id = r.region_id
WHERE m.edible ='true'
AND r.region_id IN
	(SELECT region_id
	FROM regions
	ORDER BY size DESC
	LIMIT 5);


-- Грибы категории "Пластичные", которые собираются весной в регионах размером меньше 6000
SELECT m.name
FROM mushrooms m
JOIN regions r ON m.primary_region_id = r.region_id
JOIN categories c ON m.category_id = c.category_id
WHERE m.season = 'Весна' AND c.name = 'Пластичные'
AND r.region_id IN (
    SELECT region_id
    FROM regions
    ORDER BY size <= 6000);
