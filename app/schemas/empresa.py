from pydantic import BaseModel


class EmpresaCreate(BaseModel):
    nome: str


class EmpresaResponse(BaseModel):
    id: int
    nome: str
