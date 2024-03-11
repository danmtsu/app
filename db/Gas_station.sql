USE gas_stations

CREATE TABLE gas_station (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome  VARCHAR(255),
    address VARCHAR(255) UNIQUE,
    estado VARCHAR(255),
    cidade VARCHAR(255),
    preco_etanol FLOAT,
    preco_gasolina FLOAT,
    preco_diesel FLOAT
);
