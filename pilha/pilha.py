from no import No


class Pilha:
    def __init__(self) -> None:
        self.topo = None
        self.tamanho = 0
    
    def is_empty(self):
        """Verifica o  da pilha
         retornando TRUE caso o a pilha esteja vazia ou false caso a pilha contenha alguma elemento
        """
        if self.tamanho == 0 :
            return True
        return False

    def push(self):
        pass
    
    def pop(self):
        pass

    def peek(self):
        pass

    def list_items(self):
        pass

    def get_size(self):
        return self.tamanho