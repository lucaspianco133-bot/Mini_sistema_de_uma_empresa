import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "empresa.db")

cursor = conexao.cursor()


def criar_tabela_empresa(cursor, conexao):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Empresa(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL
        )
        """
    )
    conexao.commit()


# Primary key vem antes no autoincrement


def criar_tabela_funcionario(cursor, conexao):
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS funcionario(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT, salario NUMERIC(10,2),
        tipo_de_cargo TEXT NOT NULL,
        empresa_id INTEGER,
        FOREIGN KEY (empresa_id) REFERENCES Empresa(id)
        )
        """
    )
    conexao.commit()


criar_tabela_empresa(cursor, conexao)
criar_tabela_funcionario(cursor, conexao)
