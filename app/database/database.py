import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


def conexao_db():
    conexao = sqlite3.connect(ROOT_PATH / "empresa.db")
    cursor = conexao.cursor()
    # Foring Key não ariva sozinha
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao, cursor


def criar_tabelas(cursor, conexao):
    # Primary key vem antes no autoincrement
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS Empresa(
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome TEXT NOT NULL
        )
        """
    )

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
    conexao.close()
