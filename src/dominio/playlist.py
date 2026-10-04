from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError

class Playlist:
    def __init__(self, tope=15):
        self._playlistcanciones = ListaEnlazada()
        self._tope = tope
 
    def agregar(self, cancion):
        if self._playlistcanciones.tamanio() >= self._tope:
            raise ColeccionLlenaError(f"La playlist está llena (máximo: {self._tope}).")
        
        self._playlistcanciones.insertar_al_final(cancion)
        
    def eliminar(self, cancion):
        self._playlistcanciones.eliminar(cancion)
        
    def listar(self):
        for p in self._playlistcanciones:
            print(p)

playlist = Playlist()