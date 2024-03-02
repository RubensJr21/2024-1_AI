from .local import Local
from .ambiente import Ambiente
from random import randint

class Robo:
    def __init__(self, local:Local) -> None:
        self._local:Local = local
        self._ambiente_atual:Ambiente = local[randint(0,len(local)-1)]
        self._ambientes_visitados:list = []
    
    def _limpar_ambiente(self):
        if(self._ambiente_atual.estah_sujo()):
            self._ambiente_atual.limpar()
            print(f'{self.__class__.__name__}::Limpou {self._ambiente_atual.__class__.__name__}')
        else:
            print(f'{self.__class__.__name__}::Não limpou {self._ambiente_atual.__class__.__name__}, já estava limpo')
    
    def _mover_esquerda(self):
        index = self._local.index(self._ambiente_atual)
        self._ambiente_atual = self._local[index-1]
        print(f'{self.__class__.__name__}::Moveu para a esquerda')
    
    def _mover_direita(self):
        index = self._local.index(self._ambiente_atual)
        self._ambiente_atual = self._local[index+1]
        print(f'{self.__class__.__name__}::Moveu para a direita')

    def limpar_local(self):
        while(True):
            if(not self._ambientes_visitados.__contains__(self._ambiente_atual)):
                self._limpar_ambiente()
                self._ambientes_visitados.append(self._ambiente_atual)
                if(self._ambiente_atual.get_nome() == "Ambiente A"):
                    self._mover_direita()
                elif(self._ambiente_atual.get_nome() == "Ambiente B"):
                    self._mover_esquerda()
            else:
                print(f'{self.__class__.__name__}::Limpou todos os ambientes')
                break