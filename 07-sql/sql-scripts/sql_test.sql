CREATE TABLE people (
	person_name varchar(30),
	has_pet boolean DEFAULT FALSE,
	pet_type varchar(10) NOT NULL,
	pet_name varchar(30), 
	pet_age int 
);

INSERT INTO people (person_name, has_pet, pet_type, pet_name, pet_age) 
VALUES ('Alexis', true, 'dog', 'bentley', 1),
	   ('Liana',true, 'dog', 'max', 1),
 	   ('Manpreet', true, 'cat', 'tom', 1);
	   
SELECT * FROM 
people

SELECT pet_type, pet_name
FROM people
WHERE pet_type = 'dog'
AND pet_age < 5;
