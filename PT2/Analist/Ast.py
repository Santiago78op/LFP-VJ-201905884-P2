class AST():
    
    def __init__(self,valor,tipo) -> None:
        self.id = 0
        self.tipo = tipo
        self.valor = valor
        self.hijos = list()
    