from faker import Faker
import mysql.connector
import random

# Estabelecer a conexão com o banco de dados
conexao = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="test",
    password="test",
    database="test",
    auth_plugin='mysql_native_password'
)

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()
fake = Faker()

cursor.execute('USE test')

# Popular a tabela cliente
for _ in range(100):
    nome = fake.name()
    email = fake.email()
    cpf = fake.random_int(1000000000,9000000000)
    telefone = fake.random_int(1000000000,9000000000)
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=100)


    cursor.execute(
        f"INSERT INTO cliente (nome, email, cpf, telefone, data_nascimento) VALUES ('{nome}', '{email}', '{cpf}', '{telefone}', '{data_nascimento}')"
    )

# Popular a tabela vendedor
for _ in range(5):
    nome = fake.name()
    email = fake.email()
    cpf = fake.random_int(1000000000,9000000000)
    telefone = fake.random_int(1000000000,9000000000)
    data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=33)


    cursor.execute(
        f"INSERT INTO vendedor (nome, email, cpf, telefone, data_nascimento) VALUES ('{nome}', '{email}', '{cpf}', '{telefone}', '{data_nascimento}')"
    )


# Popular a tabela livro 
for _ in range(60):
    nome = fake.word()
    categoria = fake.random_element(elements=("romance", "ficcao", "terror", "suspense", "biografia"))
    descricao = fake.text()
    valor = fake.random_int(100, 1000)

    cursor.execute(
         f"INSERT INTO livro (nome, categoria, descricao, valor) VALUES ('{nome}','{categoria}', '{descricao}', {valor})"
     )

# Primeiro, obtenha todos os IDs  existentes
cursor.execute("SELECT id FROM cliente")
cliente_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM vendedor")
vendedor_ids = [row[0] for row in cursor.fetchall()]

cursor.execute("SELECT id FROM livro")
livro_ids = [row[0] for row in cursor.fetchall()]


# Popular a tabela transacoes
for _ in range(399):
    id_cliente = random.choice(cliente_ids)
    id_vendedor = random.choice(vendedor_ids)
    id_livro = random.choice(livro_ids)
    metodo_pagamento = fake.random_element(elements=("cartao", "boleto", "pix"))
    descricao = fake.text()

    cursor.execute(
        f"INSERT INTO transacoes (id_livro, id_vendedor,  id_cliente, metodo_pagamento, descricao) VALUES ({id_livro}, {id_vendedor},  {id_cliente}, '{metodo_pagamento}', '{descricao}')"
    )

# Confirmar as alterações no banco de dados
conexao.commit()

# Fechar a conexão e o cursor
cursor.close()
conexao.close()
