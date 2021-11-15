from typing import List, NewType, Dict

FaixaDeHorario = NewType("FaixaDeHorario", str)
Materia = NewType("Materia", str)
DiaDaSemana = NewType("DiaDaSemana", str)
professor_a = NewType("professor", str)


class Aula(object):

    def __init__(self, numero: int, professor: str):
        self.num = numero
        self.professor = professor_a
        pass


class Turma(object):

    def __init__(self, nome: str, aulas: Dict[str, Aula]):
        self.nome = nome
        self.dias_da_semana = {"segunda": [Aula(numero=1, professor='professor_a')],
                               "terça": [Aula()],
                               "quarta": [Aula()]}


class Professor(object):
    def __init__(
            self, disciplinas: List[Materia],
    ) -> None:
        self.disciplinas = disciplinas

    @property
    def quantidade_de_disciplinas(self) -> int:
        return len(self.disciplinas)


prof_a = Professor(disciplinas=[Materia("Portugues")])


def validar_insercao_de_aulas(turma, aula_a_ser_inserida):
    # Uma turma não pode ter um horario ocupado no mesmo dia de semana mais de uma vez
    pass

def verificar_aulas_duplas(turma, aula_a_ser_inserida):
    # Evitar aulas duplas (seguidas)
    pass

def verificar_aulas_dias_seguidos(turma, aula_a_ser_inserida):
    # Evitar aulas em dias seguidos
    pass

def limite_aulas_diarias(turma, quantidade_aulas_diarias):
    # Limite de 8 aulas diarias
    pass

def limite_aulas_diarias_por_materia(turma, quantidade_aulas_por_materia):
    # Evitar mais de 2 aulas da mesma materia no mesmo dia
    pass

def distribuicao_materias_por_peso(materia, peso):
    # Atribuir pesos as aulas e intercalar aulas mais pesadas com aulas mais leves
    pass

def distribuicao_aulas_vagas(aula, materia):
    # Evitar janelas - Deixando as aulas vagas de preferencia nas 1º ou 6º aulas
    # Redação pode ter pelo menos 1 janela
    pass



# Fund I professora regente precisa estar presente nas 1º e 5º aulas

# Fund I - Não colocar mais de uma aula de especialista por dia.

''' Iniciamos o horário pelos professores com mais restrições nos horários.
Os sistemas já utilizados:
- Deixam muitas janelas
- Distribui as aulas de maneira pesada, muitas aulas SEGUIDAS de uma mesma disciplina 
- Não alterna aulas mais leves com aulas mais pesadas
'''



