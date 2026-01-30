class Funcionario:
    def __init__(self, nome, _salario):
        self.nome = nome
        self._salario = _salario

    @property
    def salario(self):
        return self._salario

    @salario.setter  # setter não retorna valor
    def salario(self, valor):
        if valor > 0:
            self._salario = valor
