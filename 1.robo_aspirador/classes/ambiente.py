from random import randint

class Ambiente:
    def __init__(self, nome:str) -> None:
        self._nome = nome
        self._limpo = True if randint(0,1) == 0 else False
    
    def limpar(self):
        self._limpo = True
    
    def estah_sujo(self):
        return self._limpo == False
    
    def get_nome(self):
        return self._nome
    
class AmbienteA(Ambiente):
    def __init__(self) -> None:
        super().__init__("Ambiente A")

class AmbienteB(Ambiente):
    def __init__(self) -> None:
        super().__init__("Ambiente B")