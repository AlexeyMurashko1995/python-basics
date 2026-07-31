CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    client_name TEXT,
    city TEXT,
    weight_kg REAL,
    status TEXT,
    created_at TEXT
);

INSERT INTO orders (client_name, city, weight_kg, status, created_at)
VALUES
('DHL', 'Warsaw', 150.5, 'delivered', '2026-03-01'),
('Express', 'Krakow', 80.0, 'delivered', '2026-03-02'),
('FastLog', 'Warsaw', 45.0, 'delivered', '2026-03-03'),
('CargoPlus', 'Gdansk', 200.0, 'in_transit', '2026-03-04'),
('EcoTrans', 'Krakow', 30, 'delivered', '2026-03-05')