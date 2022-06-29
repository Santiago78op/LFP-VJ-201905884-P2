class Error():

    def __init__(self, fila: int, col: int, type: str, description: str) -> None:
        self.fila = fila
        self.col = col
        self.type = type
        self.description = description

    def toString(self) -> str:
        c = self.caracter.replace('\n', r'\n')
        return f'Error en: ({str(self.fila)}, {str(self.col)}) -> " {c} "'
