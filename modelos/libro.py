class Libro:
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        # título y autor como tupla inmutable
        self._info = (titulo, autor)
        self._categoria = categoria
        self._isbn = isbn

    @property
    def info(self):
        return self._info

    @property
    def categoria(self):
        return self._categoria

    @property
    def isbn(self):
        return self._isbn

    def __str__(self):
        return f"{self._info[0]} por {self._info[1]} (ISBN: {self._isbn}, Categoría: {self._categoria})"
