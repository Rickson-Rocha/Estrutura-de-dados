class RepresentacaoCartesiana:
    def __init__(self,real:str,imaginario:str) -> None:
        self.real = real
        self.imaginario = imaginario

    def __str__(self) -> str:
        if self.imaginario > 0:
            return f'{self.real}+{self.imaginario}'
        return f'{self.real}-{self.imaginario}'