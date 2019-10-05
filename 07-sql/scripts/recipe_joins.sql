DROP TABLE ingredient;
CREATE TABLE ingredient (
	ID SERIAL,
	name varchar(30),
	units varchar(10),
	price_per_unit decimal,
	PRIMARY KEY (name)
	);
	
INSERT INTO ingredient (name, units, price_per_unit)
	VALUES ('milk','litres',1.50),
			('flour','kilograms',3.00),
			('sugar','kilograms',4.00),
			('baking soda','grams',0.05),
			('corn flour','grams',2.50);

DROP TABLE recipe_ingredient;
			 
CREATE TABLE recipe_ingredient (
	recipe_name varchar(30),
	ingredient_number int,
	ingredient_name varchar(30), -- note, not a foreign key constraint
	quantity int,
	PRIMARY KEY (recipe_name,ingredient_number)
	);

			 			 
INSERT INTO recipe_ingredient (recipe_name, ingredient_number, ingredient_name, quantity) 
	VALUES  
		('cake',1,'flour',0.5),
		('cake',2,'sugar',0.25),
		('cake',3,'milk',0.5),
		('cake',4,'baking soda',100),
		('cake',5,'butter',0.5),
		('cookies',1,'butter',0.15),
		('cookies',2,'flour',0.1),
		('cookies',3,'sugar',0.33),
		('roux',1,'butter',0.15),
		('roux',2,'flour',0.1);
	
	
SELECT * 
FROM ingredient;

SELECT * 
FROM recipe_ingredient;

-- INNER JOIN
SELECT ingredient.*, recipe_ingredient.*
FROM ingredient 
INNER JOIN recipe_ingredient 
	ON ingredient.name = recipe_ingredient.ingredient_name;
	

-- LEFT JOIN
SELECT ingredient.*, recipe_ingredient.*
FROM ingredient 
LEFT JOIN recipe_ingredient 
	ON ingredient.name = recipe_ingredient.ingredient_name;
	
	
-- RIGHT JOIN
SELECT ingredient.*, recipe_ingredient.*
FROM ingredient 
RIGHT JOIN recipe_ingredient 
	ON ingredient.name = recipe_ingredient.ingredient_name;
	

-- OUTER JOIN
SELECT ingredient.*, recipe_ingredient.*
FROM ingredient 
FULL JOIN recipe_ingredient 
	ON ingredient.name = recipe_ingredient.ingredient_name;

-- Cross JOIN
SELECT ingredient.*, recipe_ingredient.*
FROM ingredient 
CROSS JOIN recipe_ingredient;
	;--ON ingredient.name = recipe_ingredient.ingredient_name; -- do not specify ON clause for X-join


