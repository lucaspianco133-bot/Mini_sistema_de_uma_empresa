# 🏢 Mini Sistema de Empresa – FastAPI + SQLite

Este projeto é um **mini sistema de gestão de empresas e funcionários**, desenvolvido com foco **exclusivo em aprendizado**, para praticar na prática tudo o que é ensinado em cursos de backend (como os da DIO).

---

## Objetivo do Projeto

Este projeto tem como objetivo:

- Aprender FastAPI do zero
- Trabalhar com banco de dados SQLite
- Entender a separação correta de responsabilidades no backend
- Praticar Programação Orientada a Objetos (POO)
- Treinar schemas com Pydantic
- Integrar API + banco de dados passo a passo

Este projeto não é focado em produção, e sim em aprendizado real.

---

## Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- SQLite
- Pydantic
- POO
- Uvicorn

---

## Estrutura do Projeto

```text
app/
├── main.py               # Inicialização da aplicação FastAPI
├── database/
│   └── database.py       # Conexão com SQLite e criação das tabelas
├── models/               # Classes do domínio (Empresa, Funcionario, Gerente, RH)
├── schemas/              # Schemas Pydantic (request / response)
├── repositories/         # Funções SQL (insert, select, update, delete)
├── routes/               # Rotas da API (FastAPI)
└── empresa.db            # Banco de dados SQLite
```

