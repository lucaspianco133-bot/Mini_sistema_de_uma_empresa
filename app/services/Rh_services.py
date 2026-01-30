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
