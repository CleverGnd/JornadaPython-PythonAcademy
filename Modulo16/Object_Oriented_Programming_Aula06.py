# Herança múltipla

from random import choice


class Desenvolvedor:  # Exemplo aula
    def __init__(self, linguagens_programacao=None):
        self.linguagens_programacao = linguagens_programacao
        print(f'Novo Desenvolvedor com expertise nas Linguagens: \n\t{self.linguagens_programacao}')

    def desenvolver_codigo(self): print(f'Pssssssiu! Dev codando em {choice(self.linguagens_programacao)}!')


class Gerente:
    def __init__(self, softskills=None):
        self.softskills = softskills
        print(f'Novo Gerente com habilidade nas SoftSkills: \n\t{self.softskills}')

    def gerenciar_equipe(self):
        print(f'Gerente está utilizando {choice(self.softskills)} para gerenciar sua equipe!')


class TechLead(Desenvolvedor, Gerente):  # Herança múltipla
    def __init__(self, linguagens_programacao=None, softskills=None):
        Desenvolvedor.__init__(self, linguagens_programacao)  # Super não funciona, precisamos aplicar individualmente
        Gerente.__init__(self, softskills)


# Testando:
tech_lead = TechLead(['C', 'C++', 'Python'], ['Liderança', 'Comunicação Ativa', 'Feedbacks Positivos'])
tech_lead.desenvolver_codigo()
tech_lead.gerenciar_equipe()
