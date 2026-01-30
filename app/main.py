from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.database import criar_tabelas, conexao_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    conexao, cursor = conexao_db()
    criar_tabelas(cursor, conexao)
    print("Tabelas criadas com sucesso!")
    yield
    conexao.close()
    print("Finalizando aplicação...")


app = FastAPI(lifespan=lifespan)
