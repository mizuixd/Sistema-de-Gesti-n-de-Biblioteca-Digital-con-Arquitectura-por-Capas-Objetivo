class Usuario:
    def __init__(self, nombre: str, id_usuario: str):
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._libros_prestados = []  # lista de libros prestados

    @property
    def nombre(self):
        return self._nombre

    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def libros_prestados(self):
        return self._libros_prestados

    def prestar_libro(self, libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self, isbn: str):
        self._libros_prestados = [libro for libro in self._libros_prestados if libro.isbn != isbn]

    def __str__(self):
        return f"Usuario: {self._nombre} (ID: {self._id_usuario})"
