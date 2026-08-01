CREATE TABLE sales (
    id INTEGER PRIMARY KEY,
    branch TEXT,
    amount REAL,
    payment_type TEXT
);

INSERT INTO sales (branch, amount, payment_type)
VALUES
('Center', 15.0, 'card'),
('Center', 120.0, 'card'),
('North', 45.0, 'cash'),
('North', 200.0, 'card'),
('South', 30.0, 'cash'),
('South', 150.0, 'card'),
('Center', 10.0, 'cash');