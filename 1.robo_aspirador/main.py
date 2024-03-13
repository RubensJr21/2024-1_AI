# Nome do Aluno/a: Rubens do Nascimento Corrêa Júnior
# Disciplina/semestre: Inteligência Artificial/2024-1
# Turma: 37971
# Professor: Sergio Nery Simões

from classes.local import Local
from classes.ambiente import AmbienteA, AmbienteB
from classes.robo import Robo

def main():
    local:Local = [AmbienteA(), AmbienteB()]

    r = Robo(local)
    r.limpar_local()

if __name__ == "__main__":
    main()