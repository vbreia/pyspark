import mysql.connector

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

# Extrair dados da tabela clientes
cursor.execute("SELECT * FROM cliente")
cliente = cursor.fetchall()

with open("lake/clientes.csv", "w") as arquivo:
    arquivo.write("id,nome,email,cpf,telefone,ano_nascimento,mes_nascimento,dia_nascimento\n")
    for cliente in cliente:
        cliente = str(cliente).replace("(", "").replace(")", "").replace("datetime.date", "").replace("'", "")
        arquivo.write(cliente + "\n")

# Extrair dados da tabela vendedor
cursor.execute("SELECT * FROM vendedor")
vendedor = cursor.fetchall()

with open("lake/vendedores.csv", "w") as arquivo:
    arquivo.write("id,nome,email,cpf,telefone,ano_nascimento,mes_nascimento,dia_nascimento\n")
    for vendedor in vendedor:
        vendedor = str(vendedor).replace("(", "").replace(")", "").replace("datetime.date", "").replace("'", "")
        arquivo.write(vendedor + "\n")


# Extrair dados da tabela livros
cursor.execute("SELECT * FROM livro")
livro = cursor.fetchall()

with open("lake/livros.csv", "w") as arquivo:
    arquivo.write("id,nome,categoria,descricao,valor\n")
    for livro in livro:
        livro = str(livro).replace("(", "").replace(")", "").replace("'", "").replace("Decimal", "")
        arquivo.write(livro + "\n")

# Extrair dados da tabela transacoes
cursor.execute("SELECT * FROM transacoes")
transacoes = cursor.fetchall()

with open("lake/transacoes.csv", "w") as arquivo:
    arquivo.write("id,id_cliente,id_curso,id_livro,metodo_pagamento,descricao\n")
    for transacao in transacoes:
        transacao = str(transacao).replace("(", "").replace(")", "").replace("'", "")
        arquivo.write(transacao + "\n")