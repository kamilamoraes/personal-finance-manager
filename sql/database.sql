CREATE TABLE categorias (
    id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE transacoes (
    id INT PRIMARY KEY,
    descricao VARCHAR(200) NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    tipo VARCHAR(20) NOT NULL,
    data DATE NOT NULL,
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

INSERT INTO categorias (id, nome)
VALUES
(1, 'Salário'),
(2, 'Alimentação'),
(3, 'Moradia'),
(4, 'Transporte'),
(5, 'Lazer');

SELECT * FROM categorias;

INSERT INTO transacoes (id, descricao, valor, tipo, data, categoria_id)
VALUES
(1, 'Salário mensal', 3500.00, 'receita', '2026-09-01', 1),
(2, 'Aluguel', 1000.00, 'despesa', '2026-09-02', 3),
(3, 'Supermercado', 450.00, 'despesa', '2026-09-03', 2),
(4, 'Passagem de ônibus', 120.00, 'despesa', '2026-09-04', 4),
(5, 'Cinema', 80.00, 'despesa', '2026-09-05', 5);

SELECT * FROM transacoes;