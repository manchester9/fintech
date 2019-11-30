DROP TABLE card_holder, credit_card, merchant_category, merchant, transactions;

CREATE TABLE card_holder(
	card_id INTEGER PRIMARY KEY,
	card_name VARCHAR(100)
	);
	
CREATE TABLE credit_card(
	card_number BIGINT PRIMARY KEY,
	card_id INTEGER, 
-- 	REFERENCES card_holder(card_id)
    FOREIGN KEY (card_id) REFERENCES card_holder(card_id)
	);

CREATE TABLE merchant_category(
	merchant_category_id INTEGER PRIMARY KEY,
	merchant_category_name VARCHAR(100)
	);

CREATE TABLE merchant(
	merchant_id INTEGER PRIMARY KEY,
	merchant_name VARCHAR(100),
	merchant_category_id INT,
	FOREIGN KEY (merchant_category_id) REFERENCES merchant_category(merchant_category_id)
	);

CREATE TABLE transactions(
	transaction_id INTEGER PRIMARY KEY,
	date DATE,
	amount DECIMAL(10,2),
	card_number BIGINT,
	FOREIGN KEY (card_number) REFERENCES credit_card(card_number),
	merchant_id INTEGER,
	FOREIGN KEY (merchant_id) REFERENCES merchant(merchant_id)
	);
	
-- Count of all tables
SELECT schemaname,relname,n_live_tup 
  FROM pg_stat_user_tables 
  ORDER BY n_live_tup DESC;
