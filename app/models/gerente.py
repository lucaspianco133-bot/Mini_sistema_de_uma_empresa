from app.models.funcionario import Funcionario


class Gerente(Funcionario):
    def __init__(self, nome, _salario, bonus):
        super().__init__(nome, _salario)
        self.bonus = bonus

    def salario_bonus(self):
        salario = self._salario + self.bonus
        return f"Salário com bônus: R${salario:.2f}"

    @Funcionario.salario.setter  # setter não retorna valor
    def salario(self, valor):
        if valor > 1600:
            self._salario = valor
