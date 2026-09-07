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