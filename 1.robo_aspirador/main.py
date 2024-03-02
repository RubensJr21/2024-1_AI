from classes.local import Local
from classes.ambiente import AmbienteA, AmbienteB
from classes.robo import Robo

def main():
    local:Local = [AmbienteA(), AmbienteB()]

    r = Robo(local)
    r.limpar_local()

if __name__ == "__main__":
    main()