from .lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError

class Pila:
    """TAD pila implementado sobre ListaEnlazada."""

    def __init__(self):
        self._items = ListaEnlazada()

    def apilar(self, dato):
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVaciaError("El historial esta vacio")
        tope = self._items.buscar(self._items._cabeza.dato)
        self._items.eliminar(self._items._cabeza.dato)
        return tope.dato

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVaciaError("El historial esta vacio")
        return self._items._cabeza.dato

    def esta_vacia(self):
        return self._items.esta_vacia()

    def __iter__(self):
        return iter(self._items)