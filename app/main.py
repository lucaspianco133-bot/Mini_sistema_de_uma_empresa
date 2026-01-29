class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def mostrar_nome(self):
        return f"Empresa: {self.nome}"


class RH:
    def __init__(self, nome, empresa):
        self.nome = nome
        self.empresa = empresa

    def adicionar_funcionario(self, funcionario):
        self.empresa.funcionarios.append(funcionario)

    def mostrar_funcionarios(self):
        for todos_funcionarios in self.empresa.funcionarios:
            print(
                f"Funcionário: {todos_funcionarios.nome} - Salário: R${todos_funcionarios.salario:.2f}"
            )


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
