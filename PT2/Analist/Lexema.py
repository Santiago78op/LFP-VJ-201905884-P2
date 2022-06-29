class Lexema():

    def __init__(self, valor: str, descripcion: str, fila: int, col: int, patron: str) -> None:
        self.descripcion = descripcion
        self.valor = valor
        self.fila = fila
        self.col = col
        self.patron = patron
