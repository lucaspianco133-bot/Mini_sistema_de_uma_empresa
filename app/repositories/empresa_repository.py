from app.database.database import conexao_db


def criar_empresa(nome: str):
    conexao, cursor = conexao_db

    cursor.execute("INSERT INTO Empresa (nome) VALUES(?)", (nome,))
    conexao.commit()
    conexao.close()


def listar_empresa():
    conexao, cursor = conexao_db

    cursor.execute("SELECT * FROM Empresa")
    empresa = cursor.fetchall

    conexao.close()
    return empresa


def buscar_empresa_por_id(empresa_id: int, nome: str):
    conexao, cursor = conexao_db
    cursor.execute(
        "SELECT * FROM Empresa WHERE id=?,"(
            empresa_id,
        )
    )
    conexao.commit()
    conexao.close()


def atualizar_empresa(empresa_id: int, nome: str):
    conexao, cursor = conexao_db
    cursor.execute("UPDATE Empresa SET nome=?, WHERE id=?,"(nome, empresa_id))
    conexao.commit()
    conexao.close()


def deletar_empresa(empresa_id: int):
    conexao, cursor = conexao_db
    cursor.execute(
        "DELETE FROM Empresa WHERE id=?,"(
            empresa_id,
        )
    )
    conexao.commit()
    conexao.close()
