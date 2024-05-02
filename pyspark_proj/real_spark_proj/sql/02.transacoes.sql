USE `test`;

CREATE TABLE IF NOT EXISTS transacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_livro INT NOT NULL,
    id_vendedor INT NOT NULL,
    id_cliente INT NOT NULL,
    metodo_pagamento VARCHAR(20) NOT NULL,
    descricao TEXT NOT NULL,
    FOREIGN KEY (id_livro) REFERENCES livro(id),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id),
    FOREIGN KEY (id_vendedor) REFERENCES vendedor(id)
);