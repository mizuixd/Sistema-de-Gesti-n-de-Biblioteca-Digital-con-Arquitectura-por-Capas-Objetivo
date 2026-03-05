from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:
    def __init__(self):
        self._libros = {}  # diccionario {ISBN: Libro}
        self._usuarios = {}  # diccionario {ID: Usuario}
        self._ids_usuarios = set()  # conjunto para IDs únicos

    # Gestión de libros
    def agregar_libro(self, libro: Libro):
        self._libros[libro.isbn] = libro

    def quitar_libro(self, isbn: str):
        if isbn in self._libros:
            del self._libros[isbn]

    # Gestión de usuarios
    def registrar_usuario(self, usuario: Usuario):
        if usuario.id_usuario not in self._ids_usuarios:
            self._usuarios[usuario.id_usuario] = usuario
            self._ids_usuarios.add(usuario.id_usuario)

    def dar_baja_usuario(self, id_usuario: str):
        if id_usuario in self._usuarios:
            del self._usuarios[id_usuario]
            self._ids_usuarios.remove(id_usuario)

    # Préstamos
    def prestar_libro(self, id_usuario: str, isbn: str):
        if id_usuario in self._usuarios and isbn in self._libros:
            usuario = self._usuarios[id_usuario]
            libro = self._libros[isbn]
            usuario.prestar_libro(libro)
            del self._libros[isbn]

    def devolver_libro(self, id_usuario: str, isbn: str):
        if id_usuario in self._usuarios:
            usuario = self._usuarios[id_usuario]
            usuario.devolver_libro(isbn)
            # devolver al catálogo
            # (suponiendo que el libro aún existe en memoria)
            # aquí podrías guardar una copia antes de eliminarlo
            # para reinsertarlo en el diccionario

    # Búsquedas
    def buscar_por_titulo(self, titulo: str):
        return [libro for libro in self._libros.values() if libro.info[0] == titulo]

    def buscar_por_autor(self, autor: str):
        return [libro for libro in self._libros.values() if libro.info[1] == autor]

    def buscar_por_categoria(self, categoria: str):
        return [libro for libro in self._libros.values() if libro.categoria == categoria]

    def listar_libros_usuario(self, id_usuario: str):
        if id_usuario in self._usuarios:
            return self._usuarios[id_usuario].libros_prestados
        return []
