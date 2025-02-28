class Curso():
    def __init__(self, tipo: str, custo: int, semestre: str):
        self.tipo = tipo
        self.custo = custo
        self.semestre = semestre

    def exibir(self):
        print(f'Curso de {self.tipo}, {self.semestre}º semestre\nCusto do curso: {self.custo} R$')


aluno1 = Curso('engenharia da computação', 3000, '4')
aluno2 = Curso('engenharia elétrica', 3000, '4')
aluno1.exibir()
aluno2.exibir()